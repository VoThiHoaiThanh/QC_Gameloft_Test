import unittest
import requests
import csv
from tabulate import tabulate
import json
import re
import inspect


class TestResultLogger:
    def __init__(self):
        self.results = []

    def add_result(self, group, name, description, endpoint, expected, actual, status):
        self.results.append(
            {
                "Test Case Group": group,
                "Test Case Name": name,
                "Description": description,
                "Endpoint": endpoint,
                "Expected Result": expected,
                "Actual Result": actual,
                "Status": status,
            }
        )

    def get_table(self):
        return tabulate(self.results, headers="keys", tablefmt="grid")

    def save_csv(self, filename="test_results.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)
        print(f"Results saved to {filename}")

    def save_markdown(self, filename="test_results.md"):
        """Save results to a well-formatted markdown table file"""
        with open(filename, "w", encoding="utf-8") as f:
            # Write table header
            f.write("# PokéAPI Test Results\n\n")

            # Write the results table header
            f.write(
                "| Test Case Group | Test Case Name | Description | Endpoint | Status |\n"
            )
            f.write(
                "|----------------|---------------|-------------|---------|--------|\n"
            )

            # Write basic info for each test
            for result in self.results:
                # Format basic cell content for the main table
                desc = result["Description"].replace("\n", " ")
                f.write(
                    f"| {result['Test Case Group']} | {result['Test Case Name']} | {desc} | "
                )
                f.write(f"{result['Endpoint']} | {result['Status']} |\n")

            f.write("\n\n## Detailed Test Results\n\n")

            # Write detailed results for each test
            for i, result in enumerate(self.results, 1):
                f.write(
                    f"### {i}. {result['Test Case Group']} - {result['Test Case Name']}\n\n"
                )
                f.write(f"**Description:** {result['Description']}\n\n")
                f.write(f"**Endpoint:** `{result['Endpoint']}`\n\n")
                f.write(f"**Status:** {result['Status']}\n\n")

                f.write("#### Expected Result\n\n")
                f.write("```\n")
                f.write(result["Expected Result"])
                f.write("\n```\n\n")

                f.write("#### Actual Result\n\n")
                f.write("```json\n")
                f.write(result["Actual Result"])
                f.write("\n```\n\n")

                f.write("---\n\n")

            print(f"Results saved to {filename}")


logger = TestResultLogger()


def log_test_result(endpoint):
    def decorator(test_method):
        def wrapper(self, *args, **kwargs):
            # Extract test info
            test_class = self.__class__.__name__
            test_name = test_method.__name__
            test_doc = test_method.__doc__ or "No description"

            # Store the original function
            original_get = requests.get
            response_data = []

            # Extract expected values from test method source code
            source = inspect.getsource(test_method)
            expectations = []
            # Look for assertions in the code
            assertion_pattern = r"self\.assert(?:Equal|In|Greater|IsInstance|Is(?:Not)?None|True|False)\((.*?)(?:,\s*(.*?))?(?:,|\))"
            for match in re.finditer(assertion_pattern, source):
                if match.group(2):  # Two-argument assertion
                    expectations.append(
                        f"{match.group(1).strip()} should match {match.group(2).strip()}"
                    )
                else:  # One-argument assertion like assertTrue
                    expectations.append(f"{match.group(1).strip()} should be valid")

            # Create a wrapper function to capture response data
            def get_wrapper(*args, **kwargs):
                url = args[0]
                response = original_get(*args, **kwargs)

                # Always capture the API response, regardless of the endpoint
                try:
                    if response.status_code == 200:
                        # Try to parse as JSON
                        try:
                            json_data = response.json()

                            # Get endpoint name by stripping base URL if present
                            if url.startswith(self.BASE_URL):
                                actual_endpoint = url[len(self.BASE_URL) :]
                            else:
                                actual_endpoint = url

                            # Store the response data
                            response_data.append(
                                {
                                    "url": url,
                                    "endpoint": actual_endpoint,
                                    "data": json_data,
                                    "status_code": response.status_code,
                                }
                            )
                        except:
                            # Not a JSON response
                            pass
                except:
                    # Skip any errors in capturing
                    pass

                return response

            try:
                # Replace requests.get with our wrapper
                requests.get = get_wrapper

                # Run the test
                test_method(self, *args, **kwargs)

                # Format expected and actual results
                if not expectations:
                    # If we couldn't extract specific assertions, use generic message
                    expected = (
                        f"Should return valid data structure for {endpoint} requests"
                    )
                else:
                    # Use extracted assertions as expectations
                    expected = "Should return data where:\n" + "\n".join(expectations)

                if response_data:
                    # Find the most relevant response to show
                    # First try to find a response that matches our endpoint
                    endpoint_normalized = endpoint.replace("{id}", "").replace(
                        "{name}", ""
                    )
                    relevant_responses = [
                        r for r in response_data if endpoint_normalized in r["endpoint"]
                    ]

                    # If no relevant responses found, just use the first one
                    main_response = (
                        relevant_responses[0]
                        if relevant_responses
                        else response_data[0]
                    )

                    # Format the full JSON response
                    formatted_json = json.dumps(
                        main_response["data"], indent=2, ensure_ascii=False
                    )

                    # If it's too large, create a readable summary
                    if len(formatted_json) > 2000:  # Limit very large responses
                        actual = f"From {main_response['endpoint']} (Response truncated - showing key fields):\n"

                        # Create a summarized version for large responses
                        if isinstance(main_response["data"], dict):
                            summary = {}
                            # Always include id and name if they exist
                            for key in ["id", "name"]:
                                if key in main_response["data"]:
                                    summary[key] = main_response["data"][key]

                            # Add a sample of other fields
                            sample_count = 0
                            for key, value in main_response["data"].items():
                                if key not in ["id", "name"] and sample_count < 10:
                                    if isinstance(value, list):
                                        if len(value) > 2:
                                            summary[key] = [
                                                value[0],
                                                value[1],
                                                "... more items",
                                            ]
                                        else:
                                            summary[key] = value
                                    elif isinstance(value, dict):
                                        # For nested objects, include at most 3 properties
                                        sub_obj = {}
                                        sub_count = 0
                                        for sub_key, sub_val in value.items():
                                            if sub_count < 3:
                                                sub_obj[sub_key] = sub_val
                                                sub_count += 1
                                        summary[key] = sub_obj
                                    else:
                                        summary[key] = value
                                    sample_count += 1

                            actual += json.dumps(summary, indent=2, ensure_ascii=False)
                        else:
                            # For array responses
                            actual += json.dumps(
                                main_response["data"][:3], indent=2, ensure_ascii=False
                            )
                            actual += (
                                f"\n... and {len(main_response['data']) - 3} more items"
                            )
                    else:
                        # For reasonable-sized responses, show the full thing
                        actual = f"From {main_response['endpoint']}:\n{formatted_json}"

                    # Note other endpoints accessed
                    if len(response_data) > 1:
                        other_endpoints = [
                            r["endpoint"] for r in response_data if r != main_response
                        ]
                        if other_endpoints:
                            actual += f"\n\nAlso accessed: {', '.join(other_endpoints)}"
                else:
                    actual = (
                        f"No API responses were captured for this test. This might indicate:\n"
                        + f"1. The test doesn't make API calls\n"
                        + f"2. The response wasn't JSON\n"
                        + f"3. All requests failed with non-200 status codes"
                    )

                # Log success
                logger.add_result(
                    test_class,
                    test_name,
                    test_doc,
                    endpoint,
                    expected,
                    actual,
                    "✅ PASS",
                )

            except AssertionError as e:
                # For test failure
                if response_data:
                    actual = f"Failed: {str(e)}\nLast response from {response_data[-1]['endpoint']}:\n"
                    actual += json.dumps(
                        response_data[-1]["data"], indent=2, ensure_ascii=False
                    )[:1000]
                    if len(json.dumps(response_data[-1]["data"])) > 1000:
                        actual += "\n... (response truncated)"
                else:
                    actual = f"Failed: {str(e)}\nNo API response was captured"

                logger.add_result(
                    test_class,
                    test_name,
                    test_doc,
                    endpoint,
                    expected
                    if expectations
                    else f"Should return valid {endpoint} data",
                    actual,
                    "❌ FAIL",
                )
                raise
            except Exception as e:
                # For other errors
                logger.add_result(
                    test_class,
                    test_name,
                    test_doc,
                    endpoint,
                    expected
                    if expectations
                    else f"Should return valid {endpoint} data",
                    f"Error: {str(e)}",
                    "⚠️ ERROR",
                )
                raise
            finally:
                # Always restore the original function
                requests.get = original_get

        return wrapper

    return decorator


class PokemonBerryAPITest(unittest.TestCase):
    """Test cases for the Pokemon API Berry endpoint."""

    BASE_URL = "https://pokeapi.co/api/v2"

    @log_test_result("/berry/{id}")
    def test_berry_details_by_id(self):
        """Test retrieving a berry by its ID and verify its properties."""
        berry_id = 1
        response = requests.get(f"{self.BASE_URL}/berry/{berry_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "cheri")
        self.assertEqual(data["growth_time"], 3)
        self.assertEqual(data["max_harvest"], 5)
        self.assertEqual(data["natural_gift_power"], 60)
        self.assertEqual(data["size"], 20)
        self.assertEqual(data["smoothness"], 25)
        self.assertEqual(data["soil_dryness"], 15)

        self.assertIn("firmness", data)
        self.assertEqual(data["firmness"]["name"], "soft")
        self.assertTrue(data["firmness"]["url"].endswith("/berry-firmness/2/"))

        self.assertIn("flavors", data)
        self.assertIsInstance(data["flavors"], list)

        spicy_flavor = None
        for flavor in data["flavors"]:
            if flavor["flavor"]["name"] == "spicy":
                spicy_flavor = flavor
                break

        self.assertIsNotNone(spicy_flavor, "Spicy flavor not found in flavors list")
        self.assertEqual(spicy_flavor["potency"], 10)

        self.assertIn("item", data)
        self.assertEqual(data["item"]["name"], "cheri-berry")
        self.assertTrue(data["item"]["url"].endswith("/item/126/"))

        self.assertIn("natural_gift_type", data)
        self.assertEqual(data["natural_gift_type"]["name"], "fire")
        self.assertTrue(data["natural_gift_type"]["url"].endswith("/type/10/"))

    @log_test_result("/berry/{name}")
    def test_berry_details_by_name(self):
        """Test retrieving a berry by its name and compare multiple berries."""
        berry_name = "pecha"
        response = requests.get(f"{self.BASE_URL}/berry/{berry_name}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "pecha")
        self.assertIsInstance(data["growth_time"], int)
        self.assertIsInstance(data["max_harvest"], int)
        self.assertIsInstance(data["natural_gift_power"], int)

        required_fields = [
            "id",
            "name",
            "growth_time",
            "max_harvest",
            "natural_gift_power",
            "size",
            "smoothness",
            "soil_dryness",
            "firmness",
            "flavors",
            "item",
            "natural_gift_type",
        ]
        for field in required_fields:
            self.assertIn(field, data, f"Field '{field}' is missing")

        second_berry = "persim"
        response2 = requests.get(f"{self.BASE_URL}/berry/{second_berry}")
        data2 = response2.json()

        self.assertEqual(response2.status_code, 200)
        self.assertEqual(data2["name"], "persim")
        self.assertNotEqual(data["id"], data2["id"], "Berry IDs should be different")

        def get_flavor_potency(berry_data, flavor_name):
            for flavor in berry_data["flavors"]:
                if flavor["flavor"]["name"] == flavor_name:
                    return flavor["potency"]
            return 0

        sweet_potency1 = get_flavor_potency(data, "sweet")
        sweet_potency2 = get_flavor_potency(data2, "sweet")

        self.assertIsNotNone(sweet_potency1)
        self.assertIsNotNone(sweet_potency2)

        invalid_berry = "nonexistentberry12345"
        response3 = requests.get(f"{self.BASE_URL}/berry/{invalid_berry}")
        self.assertEqual(response3.status_code, 404)

    @log_test_result("/berry-firmness/{id}")
    def test_berry_firmness_endpoint(self):
        """Test the berry-firmness endpoint and verify its properties."""
        firmness_id = 1
        response = requests.get(f"{self.BASE_URL}/berry-firmness/{firmness_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "very-soft")

        self.assertIn("berries", data)
        self.assertIsInstance(data["berries"], list)
        self.assertGreater(len(data["berries"]), 0)

        pecha_found = False
        for berry in data["berries"]:
            if berry["name"] == "pecha":
                pecha_found = True
                break

        self.assertTrue(pecha_found, "Pecha berry should have very-soft firmness")

        self.assertIn("names", data)
        self.assertIsInstance(data["names"], list)

        en_name = None
        for name_entry in data["names"]:
            if name_entry["language"]["name"] == "en":
                en_name = name_entry["name"]
                break

        self.assertIsNotNone(en_name, "English name should be present")
        self.assertEqual(en_name, "Very Soft")

        response_name = requests.get(f"{self.BASE_URL}/berry-firmness/very-soft")
        data_name = response_name.json()

        self.assertEqual(data_name["id"], data["id"])
        self.assertEqual(data_name["name"], data["name"])

        response_invalid = requests.get(
            f"{self.BASE_URL}/berry-firmness/not-a-firmness"
        )
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/berry-flavor/{id}")
    def test_berry_flavor_endpoint(self):
        """Test the berry-flavor endpoint and its relationships."""
        flavor_id = 1
        response = requests.get(f"{self.BASE_URL}/berry-flavor/{flavor_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "spicy")

        self.assertIn("berries", data)
        self.assertIsInstance(data["berries"], list)
        self.assertGreater(len(data["berries"]), 0)

        first_berry = data["berries"][0]
        self.assertIn("potency", first_berry)
        self.assertIsInstance(first_berry["potency"], int)
        self.assertIn("berry", first_berry)
        self.assertIn("name", first_berry["berry"])
        self.assertIn("url", first_berry["berry"])

        self.assertIn("contest_type", data)
        self.assertIn("name", data["contest_type"])
        self.assertEqual(data["contest_type"]["name"], "cool")

        self.assertIn("names", data)
        self.assertIsInstance(data["names"], list)

        en_name = None
        for name_entry in data["names"]:
            if name_entry["language"]["name"] == "en":
                en_name = name_entry["name"]
                break

        self.assertIsNotNone(en_name, "English name should be present")
        self.assertEqual(en_name, "Spicy")

        cheri_response = requests.get(f"{self.BASE_URL}/berry/1")
        cheri_data = cheri_response.json()

        spicy_flavor = None
        for flavor in cheri_data["flavors"]:
            if flavor["flavor"]["name"] == "spicy":
                spicy_flavor = flavor
                break

        self.assertIsNotNone(spicy_flavor, "Cheri berry should have spicy flavor")
        self.assertGreater(
            spicy_flavor["potency"], 0, "Spicy flavor should have potency > 0"
        )

        response_name = requests.get(f"{self.BASE_URL}/berry-flavor/spicy")
        data_name = response_name.json()

        self.assertEqual(data_name["id"], data["id"])
        self.assertEqual(data_name["name"], data["name"])


class PokemonContestAPITest(unittest.TestCase):
    """Test cases for the Pokemon API Contest-related endpoints."""

    BASE_URL = "https://pokeapi.co/api/v2"

    @log_test_result("/contest-type/{id}")
    def test_contest_type_endpoint(self):
        """Test the contest-type endpoint and verify its properties."""
        contest_type_id = 1
        response = requests.get(f"{self.BASE_URL}/contest-type/{contest_type_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "cool")

        self.assertIn("berry_flavor", data)
        self.assertEqual(data["berry_flavor"]["name"], "spicy")
        self.assertTrue(data["berry_flavor"]["url"].endswith("/berry-flavor/1/"))

        self.assertIn("names", data)
        self.assertIsInstance(data["names"], list)
        self.assertGreater(len(data["names"]), 0)

        en_name_entry = None
        for name_entry in data["names"]:
            if name_entry["language"]["name"] == "en":
                en_name_entry = name_entry
                break

        self.assertIsNotNone(en_name_entry, "English name should be present")
        self.assertEqual(en_name_entry["name"], "Cool")
        self.assertEqual(en_name_entry["color"], "Red")

        response_name = requests.get(f"{self.BASE_URL}/contest-type/cool")
        data_name = response_name.json()

        self.assertEqual(data_name["id"], data["id"])
        self.assertEqual(data_name["name"], data["name"])

        response_invalid = requests.get(
            f"{self.BASE_URL}/contest-type/not-a-contest-type"
        )
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/contest-effect/{id}")
    def test_contest_effect_endpoint(self):
        """Test the contest-effect endpoint and verify its properties."""
        effect_id = 1
        response = requests.get(f"{self.BASE_URL}/contest-effect/{effect_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["appeal"], 4)
        self.assertEqual(data["jam"], 0)

        self.assertIn("effect_entries", data)
        self.assertIsInstance(data["effect_entries"], list)
        self.assertGreater(len(data["effect_entries"]), 0)

        en_effect = None
        for effect_entry in data["effect_entries"]:
            if effect_entry["language"]["name"] == "en":
                en_effect = effect_entry["effect"]
                break

        self.assertIsNotNone(en_effect, "English effect description should be present")
        self.assertIn("appeal points", en_effect.lower())

        self.assertIn("flavor_text_entries", data)
        self.assertIsInstance(data["flavor_text_entries"], list)
        self.assertGreater(len(data["flavor_text_entries"]), 0)

        en_flavor_text = None
        for flavor_entry in data["flavor_text_entries"]:
            if flavor_entry["language"]["name"] == "en":
                en_flavor_text = flavor_entry["flavor_text"]
                break

        self.assertIsNotNone(en_flavor_text, "English flavor text should be present")
        self.assertIn("appeal", en_flavor_text.lower())

        response_invalid = requests.get(f"{self.BASE_URL}/contest-effect/9999")
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/super-contest-effect/{id}")
    def test_super_contest_effect_endpoint(self):
        """Test the super-contest-effect endpoint and verify its properties."""
        effect_id = 1
        response = requests.get(f"{self.BASE_URL}/super-contest-effect/{effect_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["appeal"], 2)

        self.assertIn("flavor_text_entries", data)
        self.assertIsInstance(data["flavor_text_entries"], list)
        self.assertGreater(len(data["flavor_text_entries"]), 0)

        en_flavor_text = None
        for flavor_entry in data["flavor_text_entries"]:
            if flavor_entry["language"]["name"] == "en":
                en_flavor_text = flavor_entry["flavor_text"]
                break

        self.assertIsNotNone(en_flavor_text, "English flavor text should be present")
        self.assertIn("first", en_flavor_text.lower())
        self.assertIn("next turn", en_flavor_text.lower())

        self.assertIn("moves", data)
        self.assertIsInstance(data["moves"], list)
        self.assertGreater(len(data["moves"]), 0)

        agility_found = False
        for move in data["moves"]:
            if move["name"] == "agility":
                agility_found = True
                break

        self.assertTrue(agility_found, "Agility should be in moves list")

        if len(data["moves"]) > 0:
            move_name = data["moves"][0]["name"]
            move_response = requests.get(f"{self.BASE_URL}/move/{move_name}")
            move_data = move_response.json()

            if "super_contest_effect" in move_data:
                self.assertTrue(
                    move_data["super_contest_effect"]["url"].endswith(
                        f"/super-contest-effect/{effect_id}/"
                    )
                )

        response_invalid = requests.get(f"{self.BASE_URL}/super-contest-effect/9999")
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/contest-relationships")
    def test_contest_relationships(self):
        """Test relationships between contest types, berry flavors, and contest effects."""
        contest_response = requests.get(f"{self.BASE_URL}/contest-type/cool")
        contest_data = contest_response.json()

        flavor_url = contest_data["berry_flavor"]["url"]
        flavor_response = requests.get(flavor_url)
        flavor_data = flavor_response.json()

        self.assertEqual(flavor_data["name"], "spicy")
        self.assertEqual(flavor_data["contest_type"]["name"], "cool")

        move_response = requests.get(f"{self.BASE_URL}/move/agility")
        move_data = move_response.json()

        self.assertIn("contest_type", move_data)
        self.assertIn("contest_effect", move_data)
        self.assertIn("super_contest_effect", move_data)

        if "contest_effect" in move_data and move_data["contest_effect"]:
            effect_url = move_data["contest_effect"]["url"]
            effect_response = requests.get(effect_url)
            effect_data = effect_response.json()

            self.assertIn("appeal", effect_data)
            self.assertIn("jam", effect_data)


class PokemonEncounterAPITest(unittest.TestCase):
    """Test cases for the Pokemon API Encounter-related endpoints."""

    BASE_URL = "https://pokeapi.co/api/v2"

    @log_test_result("/encounter-method/{id}")
    def test_encounter_method_endpoint(self):
        """Test the encounter-method endpoint and verify its properties."""
        method_id = 1
        response = requests.get(f"{self.BASE_URL}/encounter-method/{method_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "walk")
        self.assertEqual(data["order"], 1)

        self.assertIn("names", data)
        self.assertIsInstance(data["names"], list)
        self.assertGreater(len(data["names"]), 0)

        en_name_entry = None
        for name_entry in data["names"]:
            if name_entry["language"]["name"] == "en":
                en_name_entry = name_entry
                break

        self.assertIsNotNone(en_name_entry, "English name should be present")
        self.assertEqual(en_name_entry["name"], "Walking in tall grass or a cave")

        response_name = requests.get(f"{self.BASE_URL}/encounter-method/walk")
        data_name = response_name.json()

        self.assertEqual(data_name["id"], data["id"])
        self.assertEqual(data_name["name"], data["name"])

        response_invalid = requests.get(
            f"{self.BASE_URL}/encounter-method/not-a-method"
        )
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/encounter-condition/{id}")
    def test_encounter_condition_endpoint(self):
        """Test the encounter-condition endpoint and verify its properties."""
        condition_id = 1
        response = requests.get(f"{self.BASE_URL}/encounter-condition/{condition_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "swarm")

        self.assertIn("values", data)
        self.assertIsInstance(data["values"], list)
        self.assertEqual(len(data["values"]), 2)

        value_names = [value["name"] for value in data["values"]]
        self.assertIn("swarm-yes", value_names)
        self.assertIn("swarm-no", value_names)

        self.assertIn("names", data)
        self.assertIsInstance(data["names"], list)

        de_name_entry = None
        for name_entry in data["names"]:
            if name_entry["language"]["name"] == "de":
                de_name_entry = name_entry
                break

        self.assertIsNotNone(de_name_entry, "German name should be present")
        self.assertEqual(de_name_entry["name"], "Schwarm")

        response_name = requests.get(f"{self.BASE_URL}/encounter-condition/swarm")
        data_name = response_name.json()

        self.assertEqual(data_name["id"], data["id"])
        self.assertEqual(data_name["name"], data["name"])

        response_invalid = requests.get(
            f"{self.BASE_URL}/encounter-condition/not-a-condition"
        )
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/encounter-condition-value/{id}")
    def test_encounter_condition_value_endpoint(self):
        """Test the encounter-condition-value endpoint and verify its properties."""
        value_id = 1
        response = requests.get(f"{self.BASE_URL}/encounter-condition-value/{value_id}")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "swarm-yes")

        self.assertIn("condition", data)
        self.assertEqual(data["condition"]["name"], "swarm")
        self.assertTrue(data["condition"]["url"].endswith("/encounter-condition/1/"))

        self.assertIn("names", data)
        self.assertIsInstance(data["names"], list)

        de_name_entry = None
        for name_entry in data["names"]:
            if name_entry["language"]["name"] == "de":
                de_name_entry = name_entry
                break

        self.assertIsNotNone(de_name_entry, "German name should be present")
        self.assertIn("Schwarm", de_name_entry["name"])

        response_name = requests.get(
            f"{self.BASE_URL}/encounter-condition-value/swarm-yes"
        )
        data_name = response_name.json()

        self.assertEqual(data_name["id"], data["id"])
        self.assertEqual(data_name["name"], data["name"])

        condition_url = data["condition"]["url"]
        condition_response = requests.get(condition_url)
        condition_data = condition_response.json()

        value_found = False
        for value in condition_data["values"]:
            if value["name"] == "swarm-yes":
                value_found = True
                break

        self.assertTrue(
            value_found,
            "The swarm-yes value should be in the swarm condition's values list",
        )

        response_invalid = requests.get(
            f"{self.BASE_URL}/encounter-condition-value/not-a-value"
        )
        self.assertEqual(response_invalid.status_code, 404)

    @log_test_result("/pokemon/{id}/encounters")
    def test_encounter_relationships(self):
        """Test relationships between encounter methods, conditions, and Pokemon encounters."""
        pokemon_id = 25  # Pikachu
        response = requests.get(f"{self.BASE_URL}/pokemon/{pokemon_id}/encounters")

        if response.status_code == 200 and len(response.json()) > 0:
            encounters = response.json()
            encounter = encounters[0]

            self.assertIn("location_area", encounter)
            self.assertIn("version_details", encounter)
            self.assertGreater(len(encounter["version_details"]), 0)

            version_detail = encounter["version_details"][0]
            self.assertIn("encounter_details", version_detail)
            self.assertGreater(len(version_detail["encounter_details"]), 0)

            encounter_detail = version_detail["encounter_details"][0]
            self.assertIn("method", encounter_detail)
            method_name = encounter_detail["method"]["name"]

            method_response = requests.get(
                f"{self.BASE_URL}/encounter-method/{method_name}"
            )
            self.assertEqual(method_response.status_code, 200)

            if (
                "condition_values" in encounter_detail
                and len(encounter_detail["condition_values"]) > 0
            ):
                condition_value = encounter_detail["condition_values"][0]["name"]
                value_response = requests.get(
                    f"{self.BASE_URL}/encounter-condition-value/{condition_value}"
                )
                self.assertEqual(value_response.status_code, 200)


class PokemonEvolutionAPI(unittest.TestCase):
    """Test cases for the Pokemon Evolution Chain API endpoints"""

    BASE_URL = "https://pokeapi.co/api/v2"

    def setUp(self):
        """Set up test environment"""
        self.session = requests.Session()

    @log_test_result("/evolution-chain/1/")
    def test_get_evolution_chain_by_id(self):
        """Test retrieving an evolution chain by ID"""
        response = self.session.get(f"{self.BASE_URL}/evolution-chain/1/")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("id", data)
        self.assertIn("chain", data)

        base_pokemon = data["chain"]["species"]["name"]
        self.assertEqual(base_pokemon, "bulbasaur")

        evolves_to = data["chain"]["evolves_to"]
        self.assertEqual(len(evolves_to), 1)
        self.assertEqual(evolves_to[0]["species"]["name"], "ivysaur")
        self.assertEqual(evolves_to[0]["evolves_to"][0]["species"]["name"], "venusaur")

    @log_test_result("/evolution-chain/67/")
    def test_evolution_chain_attributes(self):
        """Test evolution chain attributes and structure"""
        response = self.session.get(f"{self.BASE_URL}/evolution-chain/67/")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["chain"]["species"]["name"], "eevee")

        evolves_to = data["chain"]["evolves_to"]
        self.assertGreater(len(evolves_to), 1)

        first_evolution = evolves_to[0]
        self.assertIn("evolution_details", first_evolution)

        if len(first_evolution["evolution_details"]) > 0:
            details = first_evolution["evolution_details"][0]
            required_fields = [
                "trigger",
                "item",
                "gender",
                "held_item",
                "known_move",
                "known_move_type",
                "location",
                "min_level",
                "min_happiness",
                "min_beauty",
                "min_affection",
            ]
            for field in required_fields:
                self.assertIn(field, details)

    @log_test_result("/evolution-trigger/1/")
    def test_evolution_trigger_endpoint(self):
        """Test the evolution trigger endpoint"""
        response = self.session.get(f"{self.BASE_URL}/evolution-trigger/1/")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "level-up")

        self.assertIsInstance(data["names"], list)
        self.assertIsInstance(data["pokemon_species"], list)

    @log_test_result("/pokemon-species/machop")
    def test_chain_link_properties(self):
        """Test ChainLink properties within evolution chain"""
        response = self.session.get(f"{self.BASE_URL}/pokemon-species/machop")
        self.assertEqual(response.status_code, 200)

        species_data = response.json()
        evolution_chain_url = species_data["evolution_chain"]["url"]
        evolution_chain_id = evolution_chain_url.split("/")[-2]  # Extract ID from URL

        response = self.session.get(
            f"{self.BASE_URL}/evolution-chain/{evolution_chain_id}/"
        )
        self.assertEqual(response.status_code, 200)

        data = response.json()
        chain = data["chain"]

        self.assertIn("is_baby", chain)
        self.assertFalse(chain["is_baby"])  # Machop is not a baby Pokémon
        self.assertEqual(chain["species"]["name"], "machop")

        machoke = chain["evolves_to"][0]
        self.assertEqual(machoke["species"]["name"], "machoke")
        self.assertEqual(machoke["evolution_details"][0]["min_level"], 28)

        machamp = machoke["evolves_to"][0]
        self.assertEqual(machamp["species"]["name"], "machamp")
        trade_trigger = machamp["evolution_details"][0]["trigger"]["name"]
        self.assertEqual(trade_trigger, "trade")

    @log_test_result("/pokemon-species/wurmple")
    def test_complex_evolution_conditions(self):
        """Test Pokémon with complex evolution conditions"""
        response = self.session.get(f"{self.BASE_URL}/pokemon-species/wurmple")
        self.assertEqual(response.status_code, 200)

        species_data = response.json()
        evolution_chain_url = species_data["evolution_chain"]["url"]
        evolution_chain_id = evolution_chain_url.split("/")[-2]  # Extract ID from URL

        response = self.session.get(
            f"{self.BASE_URL}/evolution-chain/{evolution_chain_id}/"
        )
        self.assertEqual(response.status_code, 200)

        data = response.json()
        chain = data["chain"]

        self.assertEqual(chain["species"]["name"], "wurmple")
        self.assertEqual(len(chain["evolves_to"]), 2)

        evolutions = [evolution["species"]["name"] for evolution in chain["evolves_to"]]
        self.assertIn("silcoon", evolutions)
        self.assertIn("cascoon", evolutions)

        for evolution in chain["evolves_to"]:
            if evolution["species"]["name"] == "silcoon":
                self.assertEqual(
                    evolution["evolves_to"][0]["species"]["name"], "beautifly"
                )
            elif evolution["species"]["name"] == "cascoon":
                self.assertEqual(
                    evolution["evolves_to"][0]["species"]["name"], "dustox"
                )

    @log_test_result("/pokemon-species/cleffa")
    def test_baby_pokemon_evolution(self):
        """Test baby Pokémon evolution chains"""
        response = self.session.get(f"{self.BASE_URL}/pokemon-species/cleffa")
        self.assertEqual(response.status_code, 200)

        species_data = response.json()
        evolution_chain_url = species_data["evolution_chain"]["url"]
        evolution_chain_id = evolution_chain_url.split("/")[-2]  # Extract ID from URL

        response = self.session.get(
            f"{self.BASE_URL}/evolution-chain/{evolution_chain_id}/"
        )
        self.assertEqual(response.status_code, 200)

        data = response.json()
        chain = data["chain"]

        self.assertEqual(chain["species"]["name"], "cleffa")
        self.assertTrue(chain["is_baby"])

        clefairy = chain["evolves_to"][0]
        self.assertEqual(clefairy["species"]["name"], "clefairy")
        self.assertGreater(clefairy["evolution_details"][0]["min_happiness"], 0)

        clefable = clefairy["evolves_to"][0]
        self.assertEqual(clefable["species"]["name"], "clefable")
        self.assertEqual(
            clefable["evolution_details"][0]["trigger"]["name"], "use-item"
        )

    @log_test_result("/evolution-chain/error")
    def test_evolution_chain_error_handling(self):
        """Test error handling for invalid evolution chain IDs"""
        response = self.session.get(f"{self.BASE_URL}/evolution-chain/9999/")
        self.assertEqual(response.status_code, 404)

        response = self.session.get(f"{self.BASE_URL}/evolution-chain/invalid/")
        self.assertEqual(response.status_code, 404)

    @log_test_result("/pokemon-species/dynamic")
    def test_dynamic_evolution_chain_lookup(self):
        """Test looking up evolution chains dynamically by Pokémon name"""
        pokemon_names = ["pikachu", "charizard", "gyarados", "gardevoir"]

        for name in pokemon_names:
            species_response = self.session.get(
                f"{self.BASE_URL}/pokemon-species/{name}"
            )
            self.assertEqual(species_response.status_code, 200)

            species_data = species_response.json()
            evolution_chain_url = species_data["evolution_chain"]["url"]

            chain_response = self.session.get(evolution_chain_url)
            self.assertEqual(chain_response.status_code, 200)

            chain_data = chain_response.json()
            self.assertIn("chain", chain_data)
            self.assertIn("id", chain_data)

            current = chain_data["chain"]
            while current:
                self.assertIn("species", current)
                self.assertIn("name", current["species"])

                if current["evolves_to"]:
                    current = current["evolves_to"][0]
                else:
                    break


class PokemonGamesAPITest(unittest.TestCase):
    """Test cases for the PokéAPI v2"""

    BASE_URL = "https://pokeapi.co/api/v2"

    @log_test_result("/generation/1")
    def test_get_generation_by_id(self):
        """Test retrieving a generation by its ID"""
        response = requests.get(f"{self.BASE_URL}/generation/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "generation-i")
        self.assertIn("main_region", data)
        self.assertEqual(data["main_region"]["name"], "kanto")

        pokemon_species = [p["name"] for p in data["pokemon_species"]]
        self.assertIn("bulbasaur", pokemon_species)

    @log_test_result("/generation/generation-i")
    def test_get_generation_by_name(self):
        """Test retrieving a generation by its name"""
        response = requests.get(f"{self.BASE_URL}/generation/generation-i")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

    @log_test_result("/pokedex/1")
    def test_get_pokedex_by_id(self):
        """Test retrieving a pokedex by its ID"""
        response = requests.get(f"{self.BASE_URL}/pokedex/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "national")
        self.assertTrue(data["is_main_series"])

    @log_test_result("/pokedex/kanto")
    def test_get_pokedex_by_name(self):
        """Test retrieving the Kanto pokedex"""
        response = requests.get(f"{self.BASE_URL}/pokedex/kanto")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "kanto")
        self.assertEqual(data["region"]["name"], "kanto")

        entries = data["pokemon_entries"]
        first_entry = next((e for e in entries if e["entry_number"] == 1), None)
        self.assertIsNotNone(first_entry)
        self.assertEqual(first_entry["pokemon_species"]["name"], "bulbasaur")

    @log_test_result("/version/1")
    def test_get_version_by_id(self):
        """Test retrieving a version by its ID"""
        response = requests.get(f"{self.BASE_URL}/version/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "red")
        self.assertEqual(data["version_group"]["name"], "red-blue")

    @log_test_result("/version/red")
    def test_get_version_by_name(self):
        """Test retrieving the Red version"""
        response = requests.get(f"{self.BASE_URL}/version/red")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

    @log_test_result("/version-group/1")
    def test_get_version_group_by_id(self):
        """Test retrieving a version group by its ID"""
        response = requests.get(f"{self.BASE_URL}/version-group/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "red-blue")
        self.assertEqual(data["generation"]["name"], "generation-i")

        regions = [r["name"] for r in data["regions"]]
        self.assertIn("kanto", regions)

        versions = [v["name"] for v in data["versions"]]
        self.assertIn("red", versions)
        self.assertIn("blue", versions)

    @log_test_result("/version-group/red-blue")
    def test_get_version_group_by_name(self):
        """Test retrieving the Red-Blue version group"""
        response = requests.get(f"{self.BASE_URL}/version-group/red-blue")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

    @log_test_result("/generation/error")
    def test_error_handling(self):
        """Test API error handling with invalid resource ID"""
        response = requests.get(f"{self.BASE_URL}/generation/9999")
        self.assertEqual(response.status_code, 404)

    @log_test_result("/generation")
    def test_pagination(self):
        """Test API pagination by getting all generations"""
        response = requests.get(f"{self.BASE_URL}/generation")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("count", data)
        self.assertIn("results", data)
        self.assertTrue(len(data["results"]) > 0)


class PokemonItemAPITest(unittest.TestCase):
    """Test cases for the PokéAPI v2 item-related endpoints"""

    BASE_URL = "https://pokeapi.co/api/v2"

    @log_test_result("/item/master-ball")
    def test_get_item_by_name(self):
        """Test retrieving an item by its name"""
        response = requests.get(f"{self.BASE_URL}/item/master-ball")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

        effect_entries = data["effect_entries"]
        self.assertTrue(
            any(
                "wild Pokémon without fail" in entry["effect"]
                for entry in effect_entries
            )
        )

    @log_test_result("/item-attribute/1")
    def test_get_item_attribute_by_id(self):
        """Test retrieving an item attribute by its ID"""
        response = requests.get(f"{self.BASE_URL}/item-attribute/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "countable")

        descriptions = data["descriptions"]
        self.assertTrue(
            any("count in the bag" in desc["description"] for desc in descriptions)
        )

        items = [item["name"] for item in data["items"]]
        self.assertIn("master-ball", items)

    @log_test_result("/item-attribute/countable")
    def test_get_item_attribute_by_name(self):
        """Test retrieving an item attribute by name"""
        response = requests.get(f"{self.BASE_URL}/item-attribute/countable")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

    @log_test_result("/item-category/1")
    def test_get_item_category_by_id(self):
        """Test retrieving an item category by its ID"""
        response = requests.get(f"{self.BASE_URL}/item-category/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "stat-boosts")
        self.assertEqual(data["pocket"]["name"], "battle")

    @log_test_result("/item-category/standard-balls")
    def test_get_item_category_by_name(self):
        """Test retrieving an item category by name"""
        response = requests.get(f"{self.BASE_URL}/item-category/standard-balls")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        items = [item["name"] for item in data["items"]]
        self.assertIn("master-ball", items)

    @log_test_result("/item-fling-effect/1")
    def test_get_item_fling_effect_by_id(self):
        """Test retrieving an item fling effect by its ID"""
        response = requests.get(f"{self.BASE_URL}/item-fling-effect/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "badly-poison")

        effect_entries = data["effect_entries"]
        self.assertTrue(any("poisons" in entry["effect"] for entry in effect_entries))

    @log_test_result("/item-fling-effect/flinch")
    def test_get_item_fling_effect_by_name(self):
        """Test retrieving an item fling effect by name"""
        response = requests.get(f"{self.BASE_URL}/item-fling-effect/flinch")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertTrue(len(data["items"]) > 0)

    @log_test_result("/item-pocket/1")
    def test_get_item_pocket_by_id(self):
        """Test retrieving an item pocket by its ID"""
        response = requests.get(f"{self.BASE_URL}/item-pocket/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], "misc")

        categories = [cat["name"] for cat in data["categories"]]
        self.assertIn("collectibles", categories)

    @log_test_result("/item-pocket/battle")
    def test_get_item_pocket_by_name(self):
        """Test retrieving an item pocket by name"""
        response = requests.get(f"{self.BASE_URL}/item-pocket/battle")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        categories = [cat["name"] for cat in data["categories"]]
        self.assertIn("stat-boosts", categories)

    @log_test_result("/item?limit=20&offset=0")
    def test_item_pagination(self):
        """Test item API pagination"""
        response = requests.get(f"{self.BASE_URL}/item?limit=20&offset=0")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("count", data)
        self.assertIn("results", data)
        self.assertTrue(len(data["results"]) <= 20)

        items = [item["name"] for item in data["results"]]
        self.assertIn("master-ball", items)

    @log_test_result("/item/relationships")
    def test_related_item_endpoints(self):
        """Test relationships between item-related endpoints"""
        item_response = requests.get(f"{self.BASE_URL}/item/master-ball")
        item_data = item_response.json()

        category_url = item_data["category"]["url"]
        category_response = requests.get(category_url)
        self.assertEqual(category_response.status_code, 200)
        category_data = category_response.json()

        pocket_url = category_data["pocket"]["url"]
        pocket_response = requests.get(pocket_url)
        self.assertEqual(pocket_response.status_code, 200)

        if item_data["attributes"]:
            attribute_url = item_data["attributes"][0]["url"]
            attribute_response = requests.get(attribute_url)
            self.assertEqual(attribute_response.status_code, 200)

    @log_test_result("/item/error")
    def test_error_handling(self):
        """Test API error handling with invalid resource ID"""
        response = requests.get(f"{self.BASE_URL}/item/99999")
        self.assertEqual(response.status_code, 404)


class PokemonLocationAPITest(unittest.TestCase):
    """Test cases for the PokéAPI v2 location-related endpoints"""

    BASE_URL = "https://pokeapi.co/api/v2"

    @log_test_result("/location/1")
    def test_get_location_by_id(self):
        """Test retrieving a location by its ID"""
        response = requests.get(f"{self.BASE_URL}/location/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "canalave-city")
        self.assertEqual(data["region"]["name"], "sinnoh")

        self.assertTrue(len(data["areas"]) > 0)
        areas = [area["name"] for area in data["areas"]]
        self.assertIn("canalave-city-area", areas)

    @log_test_result("/location/canalave-city")
    def test_get_location_by_name(self):
        """Test retrieving a location by its name"""
        response = requests.get(f"{self.BASE_URL}/location/canalave-city")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

        names = data["names"]
        self.assertTrue(any(name["language"]["name"] == "en" for name in names))

        self.assertTrue(len(data["game_indices"]) > 0)
        for index in data["game_indices"]:
            self.assertIn("generation", index)

    @log_test_result("/location-area/1")
    def test_get_location_area_by_id(self):
        """Test retrieving a location area by its ID"""
        response = requests.get(f"{self.BASE_URL}/location-area/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "canalave-city-area")
        self.assertEqual(data["location"]["name"], "canalave-city")

        self.assertTrue(len(data["pokemon_encounters"]) > 0)
        pokemon_found = False
        for encounter in data["pokemon_encounters"]:
            if encounter["pokemon"]["name"] == "tentacool":
                pokemon_found = True
                break
        self.assertTrue(pokemon_found, "Tentacool not found in the encounter list")

    @log_test_result("/location-area/canalave-city-area")
    def test_get_location_area_by_name(self):
        """Test retrieving a location area by name"""
        response = requests.get(f"{self.BASE_URL}/location-area/canalave-city-area")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

        self.assertTrue(len(data["encounter_method_rates"]) > 0)
        for rate in data["encounter_method_rates"]:
            self.assertIn("encounter_method", rate)
            self.assertIn("version_details", rate)

    @log_test_result("/pal-park-area/1")
    def test_get_pal_park_area_by_id(self):
        """Test retrieving a pal park area by its ID"""
        response = requests.get(f"{self.BASE_URL}/pal-park-area/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "forest")

        self.assertTrue(len(data["pokemon_encounters"]) > 0)

        caterpie_found = False
        for encounter in data["pokemon_encounters"]:
            if encounter["pokemon_species"]["name"] == "caterpie":
                caterpie_found = True
                self.assertEqual(encounter["base_score"], 30)
                self.assertEqual(encounter["rate"], 50)
                break
        self.assertTrue(
            caterpie_found, "Caterpie not found in the Pal Park encounter list"
        )

    @log_test_result("/pal-park-area/forest")
    def test_get_pal_park_area_by_name(self):
        """Test retrieving a pal park area by name"""
        response = requests.get(f"{self.BASE_URL}/pal-park-area/forest")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

        names = data["names"]
        self.assertTrue(any(name["language"]["name"] == "en" for name in names))

    @log_test_result("/region/1")
    def test_get_region_by_id(self):
        """Test retrieving a region by its ID"""
        response = requests.get(f"{self.BASE_URL}/region/1")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "kanto")
        self.assertEqual(data["main_generation"]["name"], "generation-i")

        self.assertTrue(len(data["locations"]) > 0)

        self.assertTrue(len(data["pokedexes"]) > 0)
        pokedexes = [dex["name"] for dex in data["pokedexes"]]
        self.assertIn("kanto", pokedexes)

        self.assertTrue(len(data["version_groups"]) > 0)
        version_groups = [vg["name"] for vg in data["version_groups"]]
        self.assertIn("red-blue", version_groups)

    @log_test_result("/region/kanto")
    def test_get_region_by_name(self):
        """Test retrieving a region by name"""
        response = requests.get(f"{self.BASE_URL}/region/kanto")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["id"], 1)

        names = data["names"]
        self.assertTrue(any(name["language"]["name"] == "en" for name in names))

    @log_test_result("/location?limit=20&offset=0")
    def test_location_pagination(self):
        """Test location API pagination"""
        response = requests.get(f"{self.BASE_URL}/location?limit=20&offset=0")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("count", data)
        self.assertIn("results", data)
        self.assertTrue(len(data["results"]) <= 20)

        locations = [loc["name"] for loc in data["results"]]
        self.assertIn("canalave-city", locations)

    @log_test_result("/location-area?limit=20&offset=0")
    def test_location_area_pagination(self):
        """Test location area API pagination"""
        response = requests.get(f"{self.BASE_URL}/location-area?limit=20&offset=0")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("count", data)
        self.assertIn("results", data)
        self.assertTrue(len(data["results"]) <= 20)

        location_areas = [area["name"] for area in data["results"]]
        self.assertIn("canalave-city-area", location_areas)

    @log_test_result("/location/relationships")
    def test_related_location_endpoints(self):
        """Test relationships between location-related endpoints"""
        location_response = requests.get(f"{self.BASE_URL}/location/canalave-city")
        location_data = location_response.json()

        region_url = location_data["region"]["url"]
        region_response = requests.get(region_url)
        self.assertEqual(region_response.status_code, 200)

        if location_data["areas"]:
            area_url = location_data["areas"][0]["url"]
            area_response = requests.get(area_url)
            self.assertEqual(area_response.status_code, 200)
            area_data = area_response.json()

            self.assertEqual(area_data["location"]["name"], "canalave-city")

    @log_test_result("/location/error")
    def test_error_handling(self):
        """Test API error handling with invalid resource ID"""
        response = requests.get(f"{self.BASE_URL}/location/99999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    # Run the tests
    unittest.main(exit=False)
    logger.save_markdown()
