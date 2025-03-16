# PokéAPI Test Results

| Test Case Group | Test Case Name | Description | Endpoint | Status |
|----------------|---------------|-------------|---------|--------|
| PokemonBerryAPITest | test_berry_details_by_id | Test retrieving a berry by its ID and verify its properties. | /berry/{id} | ✅ PASS |
| PokemonBerryAPITest | test_berry_details_by_name | Test retrieving a berry by its name and compare multiple berries. | /berry/{name} | ✅ PASS |
| PokemonBerryAPITest | test_berry_firmness_endpoint | Test the berry-firmness endpoint and verify its properties. | /berry-firmness/{id} | ✅ PASS |
| PokemonBerryAPITest | test_berry_flavor_endpoint | Test the berry-flavor endpoint and its relationships. | /berry-flavor/{id} | ✅ PASS |
| PokemonContestAPITest | test_contest_effect_endpoint | Test the contest-effect endpoint and verify its properties. | /contest-effect/{id} | ✅ PASS |
| PokemonContestAPITest | test_contest_relationships | Test relationships between contest types, berry flavors, and contest effects. | /contest-relationships | ✅ PASS |
| PokemonContestAPITest | test_contest_type_endpoint | Test the contest-type endpoint and verify its properties. | /contest-type/{id} | ✅ PASS |
| PokemonContestAPITest | test_super_contest_effect_endpoint | Test the super-contest-effect endpoint and verify its properties. | /super-contest-effect/{id} | ✅ PASS |
| PokemonEncounterAPITest | test_encounter_condition_endpoint | Test the encounter-condition endpoint and verify its properties. | /encounter-condition/{id} | ✅ PASS |
| PokemonEncounterAPITest | test_encounter_condition_value_endpoint | Test the encounter-condition-value endpoint and verify its properties. | /encounter-condition-value/{id} | ✅ PASS |
| PokemonEncounterAPITest | test_encounter_method_endpoint | Test the encounter-method endpoint and verify its properties. | /encounter-method/{id} | ✅ PASS |
| PokemonEncounterAPITest | test_encounter_relationships | Test relationships between encounter methods, conditions, and Pokemon encounters. | /pokemon/{id}/encounters | ✅ PASS |
| PokemonEvolutionAPI | test_baby_pokemon_evolution | Test baby Pokémon evolution chains | /pokemon-species/cleffa | ✅ PASS |
| PokemonEvolutionAPI | test_chain_link_properties | Test ChainLink properties within evolution chain | /pokemon-species/machop | ✅ PASS |
| PokemonEvolutionAPI | test_complex_evolution_conditions | Test Pokémon with complex evolution conditions | /pokemon-species/wurmple | ✅ PASS |
| PokemonEvolutionAPI | test_dynamic_evolution_chain_lookup | Test looking up evolution chains dynamically by Pokémon name | /pokemon-species/dynamic | ✅ PASS |
| PokemonEvolutionAPI | test_evolution_chain_attributes | Test evolution chain attributes and structure | /evolution-chain/67/ | ✅ PASS |
| PokemonEvolutionAPI | test_evolution_chain_error_handling | Test error handling for invalid evolution chain IDs | /evolution-chain/error | ✅ PASS |
| PokemonEvolutionAPI | test_evolution_trigger_endpoint | Test the evolution trigger endpoint | /evolution-trigger/1/ | ✅ PASS |
| PokemonEvolutionAPI | test_get_evolution_chain_by_id | Test retrieving an evolution chain by ID | /evolution-chain/1/ | ✅ PASS |
| PokemonGamesAPITest | test_error_handling | Test API error handling with invalid resource ID | /generation/error | ✅ PASS |
| PokemonGamesAPITest | test_get_generation_by_id | Test retrieving a generation by its ID | /generation/1 | ✅ PASS |
| PokemonGamesAPITest | test_get_generation_by_name | Test retrieving a generation by its name | /generation/generation-i | ✅ PASS |
| PokemonGamesAPITest | test_get_pokedex_by_id | Test retrieving a pokedex by its ID | /pokedex/1 | ✅ PASS |
| PokemonGamesAPITest | test_get_pokedex_by_name | Test retrieving the Kanto pokedex | /pokedex/kanto | ✅ PASS |
| PokemonGamesAPITest | test_get_version_by_id | Test retrieving a version by its ID | /version/1 | ✅ PASS |
| PokemonGamesAPITest | test_get_version_by_name | Test retrieving the Red version | /version/red | ✅ PASS |
| PokemonGamesAPITest | test_get_version_group_by_id | Test retrieving a version group by its ID | /version-group/1 | ✅ PASS |
| PokemonGamesAPITest | test_get_version_group_by_name | Test retrieving the Red-Blue version group | /version-group/red-blue | ✅ PASS |
| PokemonGamesAPITest | test_pagination | Test API pagination by getting all generations | /generation | ✅ PASS |
| PokemonItemAPITest | test_error_handling | Test API error handling with invalid resource ID | /item/error | ✅ PASS |
| PokemonItemAPITest | test_get_item_attribute_by_id | Test retrieving an item attribute by its ID | /item-attribute/1 | ✅ PASS |
| PokemonItemAPITest | test_get_item_attribute_by_name | Test retrieving an item attribute by name | /item-attribute/countable | ✅ PASS |
| PokemonItemAPITest | test_get_item_by_name | Test retrieving an item by its name | /item/master-ball | ✅ PASS |
| PokemonItemAPITest | test_get_item_category_by_id | Test retrieving an item category by its ID | /item-category/1 | ✅ PASS |
| PokemonItemAPITest | test_get_item_category_by_name | Test retrieving an item category by name | /item-category/standard-balls | ✅ PASS |
| PokemonItemAPITest | test_get_item_fling_effect_by_id | Test retrieving an item fling effect by its ID | /item-fling-effect/1 | ✅ PASS |
| PokemonItemAPITest | test_get_item_fling_effect_by_name | Test retrieving an item fling effect by name | /item-fling-effect/flinch | ✅ PASS |
| PokemonItemAPITest | test_get_item_pocket_by_id | Test retrieving an item pocket by its ID | /item-pocket/1 | ✅ PASS |
| PokemonItemAPITest | test_get_item_pocket_by_name | Test retrieving an item pocket by name | /item-pocket/battle | ✅ PASS |
| PokemonItemAPITest | test_item_pagination | Test item API pagination | /item?limit=20&offset=0 | ✅ PASS |
| PokemonItemAPITest | test_related_item_endpoints | Test relationships between item-related endpoints | /item/relationships | ✅ PASS |
| PokemonLocationAPITest | test_error_handling | Test API error handling with invalid resource ID | /location/error | ✅ PASS |
| PokemonLocationAPITest | test_get_location_area_by_id | Test retrieving a location area by its ID | /location-area/1 | ✅ PASS |
| PokemonLocationAPITest | test_get_location_area_by_name | Test retrieving a location area by name | /location-area/canalave-city-area | ✅ PASS |
| PokemonLocationAPITest | test_get_location_by_id | Test retrieving a location by its ID | /location/1 | ✅ PASS |
| PokemonLocationAPITest | test_get_location_by_name | Test retrieving a location by its name | /location/canalave-city | ✅ PASS |
| PokemonLocationAPITest | test_get_pal_park_area_by_id | Test retrieving a pal park area by its ID | /pal-park-area/1 | ✅ PASS |
| PokemonLocationAPITest | test_get_pal_park_area_by_name | Test retrieving a pal park area by name | /pal-park-area/forest | ✅ PASS |
| PokemonLocationAPITest | test_get_region_by_id | Test retrieving a region by its ID | /region/1 | ✅ PASS |
| PokemonLocationAPITest | test_get_region_by_name | Test retrieving a region by name | /region/kanto | ✅ PASS |
| PokemonLocationAPITest | test_location_area_pagination | Test location area API pagination | /location-area?limit=20&offset=0 | ✅ PASS |
| PokemonLocationAPITest | test_location_pagination | Test location API pagination | /location?limit=20&offset=0 | ✅ PASS |
| PokemonLocationAPITest | test_related_location_endpoints | Test relationships between location-related endpoints | /location/relationships | ✅ PASS |


## Detailed Test Results

### 1. PokemonBerryAPITest - test_berry_details_by_id

**Description:** Test retrieving a berry by its ID and verify its properties.

**Endpoint:** `/berry/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "cheri"
data["growth_time"] should match 3
data["max_harvest"] should match 5
data["natural_gift_power"] should match 60
data["size"] should match 20
data["smoothness"] should match 25
data["soil_dryness"] should match 15
"firmness" should match data
data["firmness"]["name"] should match "soft"
data["firmness"]["url"].endswith("/berry-firmness/2/" should be valid
"flavors" should match data
data["flavors"] should match list
spicy_flavor should match "Spicy flavor not found in flavors list"
spicy_flavor["potency"] should match 10
"item" should match data
data["item"]["name"] should match "cheri-berry"
data["item"]["url"].endswith("/item/126/" should be valid
"natural_gift_type" should match data
data["natural_gift_type"]["name"] should match "fire"
data["natural_gift_type"]["url"].endswith("/type/10/" should be valid
```

#### Actual Result

```json
From /berry/1:
{
  "firmness": {
    "name": "soft",
    "url": "https://pokeapi.co/api/v2/berry-firmness/2/"
  },
  "flavors": [
    {
      "flavor": {
        "name": "spicy",
        "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
      },
      "potency": 10
    },
    {
      "flavor": {
        "name": "dry",
        "url": "https://pokeapi.co/api/v2/berry-flavor/2/"
      },
      "potency": 0
    },
    {
      "flavor": {
        "name": "sweet",
        "url": "https://pokeapi.co/api/v2/berry-flavor/3/"
      },
      "potency": 0
    },
    {
      "flavor": {
        "name": "bitter",
        "url": "https://pokeapi.co/api/v2/berry-flavor/4/"
      },
      "potency": 0
    },
    {
      "flavor": {
        "name": "sour",
        "url": "https://pokeapi.co/api/v2/berry-flavor/5/"
      },
      "potency": 0
    }
  ],
  "growth_time": 3,
  "id": 1,
  "item": {
    "name": "cheri-berry",
    "url": "https://pokeapi.co/api/v2/item/126/"
  },
  "max_harvest": 5,
  "name": "cheri",
  "natural_gift_power": 60,
  "natural_gift_type": {
    "name": "fire",
    "url": "https://pokeapi.co/api/v2/type/10/"
  },
  "size": 20,
  "smoothness": 25,
  "soil_dryness": 15
}
```

---

### 2. PokemonBerryAPITest - test_berry_details_by_name

**Description:** Test retrieving a berry by its name and compare multiple berries.

**Endpoint:** `/berry/{name}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "pecha"
data["growth_time"] should match int
data["max_harvest"] should match int
data["natural_gift_power"] should match int
field should match data
response2.status_code should match 200
data2["name"] should match "persim"
sweet_potency1 should be valid
sweet_potency2 should be valid
response3.status_code should match 404
```

#### Actual Result

```json
From /berry/pecha:
{
  "firmness": {
    "name": "very-soft",
    "url": "https://pokeapi.co/api/v2/berry-firmness/1/"
  },
  "flavors": [
    {
      "flavor": {
        "name": "spicy",
        "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
      },
      "potency": 0
    },
    {
      "flavor": {
        "name": "dry",
        "url": "https://pokeapi.co/api/v2/berry-flavor/2/"
      },
      "potency": 0
    },
    {
      "flavor": {
        "name": "sweet",
        "url": "https://pokeapi.co/api/v2/berry-flavor/3/"
      },
      "potency": 10
    },
    {
      "flavor": {
        "name": "bitter",
        "url": "https://pokeapi.co/api/v2/berry-flavor/4/"
      },
      "potency": 0
    },
    {
      "flavor": {
        "name": "sour",
        "url": "https://pokeapi.co/api/v2/berry-flavor/5/"
      },
      "potency": 0
    }
  ],
  "growth_time": 3,
  "id": 3,
  "item": {
    "name": "pecha-berry",
    "url": "https://pokeapi.co/api/v2/item/128/"
  },
  "max_harvest": 5,
  "name": "pecha",
  "natural_gift_power": 60,
  "natural_gift_type": {
    "name": "electric",
    "url": "https://pokeapi.co/api/v2/type/13/"
  },
  "size": 40,
  "smoothness": 25,
  "soil_dryness": 15
}

Also accessed: /berry/persim
```

---

### 3. PokemonBerryAPITest - test_berry_firmness_endpoint

**Description:** Test the berry-firmness endpoint and verify its properties.

**Endpoint:** `/berry-firmness/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "very-soft"
"berries" should match data
data["berries"] should match list
len(data["berries"] should be valid
pecha_found should match "Pecha berry should have very-soft firmness"
"names" should match data
data["names"] should match list
en_name should match "English name should be present"
en_name should match "Very Soft"
data_name["id"] should match data["id"]
data_name["name"] should match data["name"]
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /berry-firmness/1:
{
  "berries": [
    {
      "name": "pecha",
      "url": "https://pokeapi.co/api/v2/berry/3/"
    },
    {
      "name": "pamtre",
      "url": "https://pokeapi.co/api/v2/berry/32/"
    },
    {
      "name": "belue",
      "url": "https://pokeapi.co/api/v2/berry/35/"
    },
    {
      "name": "wacan",
      "url": "https://pokeapi.co/api/v2/berry/38/"
    },
    {
      "name": "tanga",
      "url": "https://pokeapi.co/api/v2/berry/46/"
    },
    {
      "name": "charti",
      "url": "https://pokeapi.co/api/v2/berry/47/"
    },
    {
      "name": "chilan",
      "url": "https://pokeapi.co/api/v2/berry/52/"
    },
    {
      "name": "rowap",
      "url": "https://pokeapi.co/api/v2/berry/64/"
    }
  ],
  "id": 1,
  "name": "very-soft",
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "とてもやわらかい"
    },
    {
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "很柔軟"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Très tendre"
    },
    {
      "language": {
        "name": "es",
        "url": "https://pokeapi.co/api/v2/language/7/"
      },
      "name": "Muy blanda"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Very Soft"
    },
    {
      "language": {
        "name": "zh-Hans",
        "url": "https://pokeapi.co/api/v2/language/12/"
      },
      "name": "很柔软"
    }
  ]
}

Also accessed: /berry-firmness/very-soft
```

---

### 4. PokemonBerryAPITest - test_berry_flavor_endpoint

**Description:** Test the berry-flavor endpoint and its relationships.

**Endpoint:** `/berry-flavor/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "spicy"
"berries" should match data
data["berries"] should match list
len(data["berries"] should be valid
"potency" should match first_berry
first_berry["potency"] should match int
"berry" should match first_berry
"name" should match first_berry["berry"]
"url" should match first_berry["berry"]
"contest_type" should match data
"name" should match data["contest_type"]
data["contest_type"]["name"] should match "cool"
"names" should match data
data["names"] should match list
en_name should match "English name should be present"
en_name should match "Spicy"
spicy_flavor should match "Cheri berry should have spicy flavor"
data_name["id"] should match data["id"]
data_name["name"] should match data["name"]
```

#### Actual Result

```json
From /berry-flavor/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "spicy",
  "berries": [
    {
      "berry": {
        "name": "rowap",
        "url": "https://pokeapi.co/api/v2/berry/64/"
      },
      "potency": 10
    },
    {
      "berry": {
        "name": "leppa",
        "url": "https://pokeapi.co/api/v2/berry/6/"
      },
      "potency": 10
    },
    "... more items"
  ],
  "contest_type": {
    "name": "cool",
    "url": "https://pokeapi.co/api/v2/contest-type/1/"
  },
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "からい"
    },
    {
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "辣"
    },
    "... more items"
  ]
}

Also accessed: /berry/1, /berry-flavor/spicy
```

---

### 5. PokemonContestAPITest - test_contest_effect_endpoint

**Description:** Test the contest-effect endpoint and verify its properties.

**Endpoint:** `/contest-effect/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["appeal"] should match 4
data["jam"] should match 0
"effect_entries" should match data
data["effect_entries"] should match list
len(data["effect_entries"] should be valid
en_effect should match "English effect description should be present"
"appeal points" should match en_effect.lower(
"flavor_text_entries" should match data
data["flavor_text_entries"] should match list
len(data["flavor_text_entries"] should be valid
en_flavor_text should match "English flavor text should be present"
"appeal" should match en_flavor_text.lower(
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /contest-effect/1:
{
  "appeal": 4,
  "effect_entries": [
    {
      "effect": "Gives a high number of appeal points wth no other effects.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "flavor_text_entries": [
    {
      "flavor_text": "A highly appealing move.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "id": 1,
  "jam": 0
}
```

---

### 6. PokemonContestAPITest - test_contest_relationships

**Description:** Test relationships between contest types, berry flavors, and contest effects.

**Endpoint:** `/contest-relationships`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
flavor_data["name"] should match "spicy"
flavor_data["contest_type"]["name"] should match "cool"
"contest_type" should match move_data
"contest_effect" should match move_data
"super_contest_effect" should match move_data
"appeal" should match effect_data
"jam" should match effect_data
```

#### Actual Result

```json
From /contest-type/cool:
{
  "berry_flavor": {
    "name": "spicy",
    "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
  },
  "id": 1,
  "name": "cool",
  "names": [
    {
      "color": "",
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "かっこよさ"
    },
    {
      "color": "紅",
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "帥氣"
    },
    {
      "color": "Rouge",
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Sang-froid"
    },
    {
      "color": "Red",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Cool"
    },
    {
      "color": "红",
      "language": {
        "name": "zh-Hans",
        "url": "https://pokeapi.co/api/v2/language/12/"
      },
      "name": "帅气"
    }
  ]
}

Also accessed: /berry-flavor/1/, /move/agility, /contest-effect/30/
```

---

### 7. PokemonContestAPITest - test_contest_type_endpoint

**Description:** Test the contest-type endpoint and verify its properties.

**Endpoint:** `/contest-type/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "cool"
"berry_flavor" should match data
data["berry_flavor"]["name"] should match "spicy"
data["berry_flavor"]["url"].endswith("/berry-flavor/1/" should be valid
"names" should match data
data["names"] should match list
len(data["names"] should be valid
en_name_entry should match "English name should be present"
en_name_entry["name"] should match "Cool"
en_name_entry["color"] should match "Red"
data_name["id"] should match data["id"]
data_name["name"] should match data["name"]
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /contest-type/1:
{
  "berry_flavor": {
    "name": "spicy",
    "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
  },
  "id": 1,
  "name": "cool",
  "names": [
    {
      "color": "",
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "かっこよさ"
    },
    {
      "color": "紅",
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "帥氣"
    },
    {
      "color": "Rouge",
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Sang-froid"
    },
    {
      "color": "Red",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Cool"
    },
    {
      "color": "红",
      "language": {
        "name": "zh-Hans",
        "url": "https://pokeapi.co/api/v2/language/12/"
      },
      "name": "帅气"
    }
  ]
}

Also accessed: /contest-type/cool
```

---

### 8. PokemonContestAPITest - test_super_contest_effect_endpoint

**Description:** Test the super-contest-effect endpoint and verify its properties.

**Endpoint:** `/super-contest-effect/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["appeal"] should match 2
"flavor_text_entries" should match data
data["flavor_text_entries"] should match list
len(data["flavor_text_entries"] should be valid
en_flavor_text should match "English flavor text should be present"
"first" should match en_flavor_text.lower(
"next turn" should match en_flavor_text.lower(
"moves" should match data
data["moves"] should match list
len(data["moves"] should be valid
agility_found should match "Agility should be in moves list"
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /super-contest-effect/1:
{
  "appeal": 2,
  "flavor_text_entries": [
    {
      "flavor_text": "Enables the user to perform first in the next turn.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "id": 1,
  "moves": [
    {
      "name": "agility",
      "url": "https://pokeapi.co/api/v2/move/97/"
    },
    {
      "name": "quick-attack",
      "url": "https://pokeapi.co/api/v2/move/98/"
    },
    {
      "name": "teleport",
      "url": "https://pokeapi.co/api/v2/move/100/"
    },
    {
      "name": "double-team",
      "url": "https://pokeapi.co/api/v2/move/104/"
    },
    {
      "name": "cotton-spore",
      "url": "https://pokeapi.co/api/v2/move/178/"
    },
    {
      "name": "mach-punch",
      "url": "https://pokeapi.co/api/v2/move/183/"
    },
    {
      "name": "extreme-speed",
      "url": "https://pokeapi.co/api/v2/move/245/"
    },
    {
      "name": "tailwind",
      "url": "https://pokeapi.co/api/v2/move/366/"
    },
    {
      "name": "me-first",
      "url": "https://pokeapi.co/api/v2/move/382/"
    },
    {
      "name": "sucker-punch",
      "url": "https://pokeapi.co/api/v2/move/389/"
    },
    {
      "name": "rock-polish",
      "url": "https://pokeapi.co/api/v2/move/397/"
    },
    {
      "name": "vacuum-wave",
      "url": "https://pokeapi.co/api/v2/move/410/"
    },
    {
      "name": "bullet-punch",
      "url": "https://pokeapi.co/api/v2/move/418/"
    },
    {
      "name": "ice-shard",
      "url": "https://pokeapi.co/api/v2/move/420/"
    },
    {
      "name": "shadow-sneak",
      "url": "https://pokeapi.co/api/v2/move/425/"
    },
    {
      "name": "aqua-jet",
      "url": "https://pokeapi.co/api/v2/move/453/"
    }
  ]
}

Also accessed: /move/agility
```

---

### 9. PokemonEncounterAPITest - test_encounter_condition_endpoint

**Description:** Test the encounter-condition endpoint and verify its properties.

**Endpoint:** `/encounter-condition/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "swarm"
"values" should match data
data["values"] should match list
len(data["values"] should be valid
"swarm-yes" should match value_names
"swarm-no" should match value_names
"names" should match data
data["names"] should match list
de_name_entry should match "German name should be present"
de_name_entry["name"] should match "Schwarm"
data_name["id"] should match data["id"]
data_name["name"] should match data["name"]
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /encounter-condition/1:
{
  "id": 1,
  "name": "swarm",
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Essaim"
    },
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "Schwarm"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Swarm"
    }
  ],
  "values": [
    {
      "name": "swarm-yes",
      "url": "https://pokeapi.co/api/v2/encounter-condition-value/1/"
    },
    {
      "name": "swarm-no",
      "url": "https://pokeapi.co/api/v2/encounter-condition-value/2/"
    }
  ]
}

Also accessed: /encounter-condition/swarm
```

---

### 10. PokemonEncounterAPITest - test_encounter_condition_value_endpoint

**Description:** Test the encounter-condition-value endpoint and verify its properties.

**Endpoint:** `/encounter-condition-value/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "swarm-yes"
"condition" should match data
data["condition"]["name"] should match "swarm"
data["condition"]["url"].endswith("/encounter-condition/1/" should be valid
"names" should match data
data["names"] should match list
de_name_entry should match "German name should be present"
"Schwarm" should match de_name_entry["name"]
data_name["id"] should match data["id"]
data_name["name"] should match data["name"]
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /encounter-condition-value/1:
{
  "condition": {
    "name": "swarm",
    "url": "https://pokeapi.co/api/v2/encounter-condition/1/"
  },
  "id": 1,
  "name": "swarm-yes",
  "names": [
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "Während eines Schwarms"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "During a swarm"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Pendant une tempête"
    }
  ]
}

Also accessed: /encounter-condition-value/swarm-yes, /encounter-condition/1/
```

---

### 11. PokemonEncounterAPITest - test_encounter_method_endpoint

**Description:** Test the encounter-method endpoint and verify its properties.

**Endpoint:** `/encounter-method/{id}`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "walk"
data["order"] should match 1
"names" should match data
data["names"] should match list
len(data["names"] should be valid
en_name_entry should match "English name should be present"
en_name_entry["name"] should match "Walking in tall grass or a cave"
data_name["id"] should match data["id"]
data_name["name"] should match data["name"]
response_invalid.status_code should match 404
```

#### Actual Result

```json
From /encounter-method/1:
{
  "id": 1,
  "name": "walk",
  "names": [
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "Im hohen Gras oder in einer Höhle laufen"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Walking in tall grass or a cave"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "En marchant dans les herbes hautes ou une grotte"
    }
  ],
  "order": 1
}

Also accessed: /encounter-method/walk
```

---

### 12. PokemonEncounterAPITest - test_encounter_relationships

**Description:** Test relationships between encounter methods, conditions, and Pokemon encounters.

**Endpoint:** `/pokemon/{id}/encounters`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
"location_area" should match encounter
"version_details" should match encounter
len(encounter["version_details"] should be valid
"encounter_details" should match version_detail
len(version_detail["encounter_details"] should be valid
"method" should match encounter_detail
method_response.status_code should match 200
value_response.status_code should match 200
```

#### Actual Result

```json
From /pokemon/25/encounters (Response truncated - showing key fields):
[
  {
    "location_area": {
      "name": "trophy-garden-area",
      "url": "https://pokeapi.co/api/v2/location-area/118/"
    },
    "version_details": [
      {
        "encounter_details": [
          {
            "chance": 5,
            "condition_values": [],
            "max_level": 18,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 18
          },
          {
            "chance": 4,
            "condition_values": [],
            "max_level": 18,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 18
          },
          {
            "chance": 1,
            "condition_values": [],
            "max_level": 18,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 18
          }
        ],
        "max_chance": 10,
        "version": {
          "name": "diamond",
          "url": "https://pokeapi.co/api/v2/version/12/"
        }
      },
      {
        "encounter_details": [
          {
            "chance": 5,
            "condition_values": [],
            "max_level": 18,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 18
          },
          {
            "chance": 4,
            "condition_values": [],
            "max_level": 18,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 18
          },
          {
            "chance": 1,
            "condition_values": [],
            "max_level": 18,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 18
          }
        ],
        "max_chance": 10,
        "version": {
          "name": "pearl",
          "url": "https://pokeapi.co/api/v2/version/13/"
        }
      },
      {
        "encounter_details": [
          {
            "chance": 5,
            "condition_values": [],
            "max_level": 22,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 22
          },
          {
            "chance": 4,
            "condition_values": [],
            "max_level": 24,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 24
          },
          {
            "chance": 1,
            "condition_values": [],
            "max_level": 24,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 24
          }
        ],
        "max_chance": 10,
        "version": {
          "name": "platinum",
          "url": "https://pokeapi.co/api/v2/version/14/"
        }
      }
    ]
  },
  {
    "location_area": {
      "name": "pallet-town-area",
      "url": "https://pokeapi.co/api/v2/location-area/285/"
    },
    "version_details": [
      {
        "encounter_details": [
          {
            "chance": 100,
            "condition_values": [],
            "max_level": 5,
            "method": {
              "name": "gift",
              "url": "https://pokeapi.co/api/v2/encounter-method/18/"
            },
            "min_level": 5
          }
        ],
        "max_chance": 100,
        "version": {
          "name": "yellow",
          "url": "https://pokeapi.co/api/v2/version/3/"
        }
      }
    ]
  },
  {
    "location_area": {
      "name": "kanto-route-2-south-towards-viridian-city",
      "url": "https://pokeapi.co/api/v2/location-area/296/"
    },
    "version_details": [
      {
        "encounter_details": [
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-day",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/4/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-morning",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-night",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/5/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-day",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/4/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-morning",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-night",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/5/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          }
        ],
        "max_chance": 15,
        "version": {
          "name": "gold",
          "url": "https://pokeapi.co/api/v2/version/4/"
        }
      },
      {
        "encounter_details": [
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-day",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/4/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-morning",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-night",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/5/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-day",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/4/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-morning",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-night",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/5/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          }
        ],
        "max_chance": 15,
        "version": {
          "name": "silver",
          "url": "https://pokeapi.co/api/v2/version/5/"
        }
      },
      {
        "encounter_details": [
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-day",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/4/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 4,
            "condition_values": [
              {
                "name": "time-morning",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-day",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/4/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          },
          {
            "chance": 1,
            "condition_values": [
              {
                "name": "time-morning",
                "url": "https://pokeapi.co/api/v2/encounter-condition-value/3/"
              }
            ],
            "max_level": 4,
            "method": {
              "name": "walk",
              "url": "https://pokeapi.co/api/v2/encounter-method/1/"
            },
            "min_level": 4
          }
        ],
        "max_chance": 10,
        "version": {
          "name": "crystal",
          "url": "https://pokeapi.co/api/v2/version/6/"
        }
      }
    ]
  }
]
... and 14 more items

Also accessed: /encounter-method/walk
```

---

### 13. PokemonEvolutionAPI - test_baby_pokemon_evolution

**Description:** Test baby Pokémon evolution chains

**Endpoint:** `/pokemon-species/cleffa`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
response.status_code should match 200
chain["species"]["name"] should match "cleffa"
chain["is_baby"] should be valid
clefairy["species"]["name"] should match "clefairy"
clefairy["evolution_details"][0]["min_happiness"] should match 0
clefable["species"]["name"] should match "clefable"
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 14. PokemonEvolutionAPI - test_chain_link_properties

**Description:** Test ChainLink properties within evolution chain

**Endpoint:** `/pokemon-species/machop`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
response.status_code should match 200
"is_baby" should match chain
chain["is_baby"] should be valid
chain["species"]["name"] should match "machop"
machoke["species"]["name"] should match "machoke"
machoke["evolution_details"][0]["min_level"] should match 28
machamp["species"]["name"] should match "machamp"
trade_trigger should match "trade"
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 15. PokemonEvolutionAPI - test_complex_evolution_conditions

**Description:** Test Pokémon with complex evolution conditions

**Endpoint:** `/pokemon-species/wurmple`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
response.status_code should match 200
chain["species"]["name"] should match "wurmple"
len(chain["evolves_to"] should be valid
"silcoon" should match evolutions
"cascoon" should match evolutions
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 16. PokemonEvolutionAPI - test_dynamic_evolution_chain_lookup

**Description:** Test looking up evolution chains dynamically by Pokémon name

**Endpoint:** `/pokemon-species/dynamic`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
species_response.status_code should match 200
chain_response.status_code should match 200
"chain" should match chain_data
"id" should match chain_data
"species" should match current
"name" should match current["species"]
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 17. PokemonEvolutionAPI - test_evolution_chain_attributes

**Description:** Test evolution chain attributes and structure

**Endpoint:** `/evolution-chain/67/`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["chain"]["species"]["name"] should match "eevee"
len(evolves_to should be valid
"evolution_details" should match first_evolution
field should match details
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 18. PokemonEvolutionAPI - test_evolution_chain_error_handling

**Description:** Test error handling for invalid evolution chain IDs

**Endpoint:** `/evolution-chain/error`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 404
response.status_code should match 404
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 19. PokemonEvolutionAPI - test_evolution_trigger_endpoint

**Description:** Test the evolution trigger endpoint

**Endpoint:** `/evolution-trigger/1/`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "level-up"
data["names"] should match list
data["pokemon_species"] should match list
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 20. PokemonEvolutionAPI - test_get_evolution_chain_by_id

**Description:** Test retrieving an evolution chain by ID

**Endpoint:** `/evolution-chain/1/`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"id" should match data
"chain" should match data
base_pokemon should match "bulbasaur"
len(evolves_to should be valid
evolves_to[0]["species"]["name"] should match "ivysaur"
evolves_to[0]["evolves_to"][0]["species"]["name"] should match "venusaur"
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 21. PokemonGamesAPITest - test_error_handling

**Description:** Test API error handling with invalid resource ID

**Endpoint:** `/generation/error`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 404
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 22. PokemonGamesAPITest - test_get_generation_by_id

**Description:** Test retrieving a generation by its ID

**Endpoint:** `/generation/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "generation-i"
"main_region" should match data
data["main_region"]["name"] should match "kanto"
"bulbasaur" should match pokemon_species
```

#### Actual Result

```json
From /generation/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "generation-i",
  "abilities": [],
  "main_region": {
    "name": "kanto",
    "url": "https://pokeapi.co/api/v2/region/1/"
  },
  "moves": [
    {
      "name": "pound",
      "url": "https://pokeapi.co/api/v2/move/1/"
    },
    {
      "name": "karate-chop",
      "url": "https://pokeapi.co/api/v2/move/2/"
    },
    "... more items"
  ],
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "だいいちせだい"
    },
    {
      "language": {
        "name": "ko",
        "url": "https://pokeapi.co/api/v2/language/3/"
      },
      "name": "1세대"
    },
    "... more items"
  ],
  "pokemon_species": [
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
    },
    {
      "name": "charmander",
      "url": "https://pokeapi.co/api/v2/pokemon-species/4/"
    },
    "... more items"
  ],
  "types": [
    {
      "name": "normal",
      "url": "https://pokeapi.co/api/v2/type/1/"
    },
    {
      "name": "fighting",
      "url": "https://pokeapi.co/api/v2/type/2/"
    },
    "... more items"
  ],
  "version_groups": [
    {
      "name": "red-blue",
      "url": "https://pokeapi.co/api/v2/version-group/1/"
    },
    {
      "name": "yellow",
      "url": "https://pokeapi.co/api/v2/version-group/2/"
    }
  ]
}
```

---

### 23. PokemonGamesAPITest - test_get_generation_by_name

**Description:** Test retrieving a generation by its name

**Endpoint:** `/generation/generation-i`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
```

#### Actual Result

```json
From /generation/generation-i (Response truncated - showing key fields):
{
  "id": 1,
  "name": "generation-i",
  "abilities": [],
  "main_region": {
    "name": "kanto",
    "url": "https://pokeapi.co/api/v2/region/1/"
  },
  "moves": [
    {
      "name": "pound",
      "url": "https://pokeapi.co/api/v2/move/1/"
    },
    {
      "name": "karate-chop",
      "url": "https://pokeapi.co/api/v2/move/2/"
    },
    "... more items"
  ],
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "だいいちせだい"
    },
    {
      "language": {
        "name": "ko",
        "url": "https://pokeapi.co/api/v2/language/3/"
      },
      "name": "1세대"
    },
    "... more items"
  ],
  "pokemon_species": [
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
    },
    {
      "name": "charmander",
      "url": "https://pokeapi.co/api/v2/pokemon-species/4/"
    },
    "... more items"
  ],
  "types": [
    {
      "name": "normal",
      "url": "https://pokeapi.co/api/v2/type/1/"
    },
    {
      "name": "fighting",
      "url": "https://pokeapi.co/api/v2/type/2/"
    },
    "... more items"
  ],
  "version_groups": [
    {
      "name": "red-blue",
      "url": "https://pokeapi.co/api/v2/version-group/1/"
    },
    {
      "name": "yellow",
      "url": "https://pokeapi.co/api/v2/version-group/2/"
    }
  ]
}
```

---

### 24. PokemonGamesAPITest - test_get_pokedex_by_id

**Description:** Test retrieving a pokedex by its ID

**Endpoint:** `/pokedex/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "national"
data["is_main_series"] should be valid
```

#### Actual Result

```json
From /pokedex/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "national",
  "descriptions": [
    {
      "description": "Pokédex National complet",
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      }
    },
    {
      "description": "Komplette Nationale Dex",
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      }
    },
    "... more items"
  ],
  "is_main_series": true,
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "National"
    },
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "National"
    },
    "... more items"
  ],
  "pokemon_entries": [
    {
      "entry_number": 1,
      "pokemon_species": {
        "name": "bulbasaur",
        "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
      }
    },
    {
      "entry_number": 2,
      "pokemon_species": {
        "name": "ivysaur",
        "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
      }
    },
    "... more items"
  ],
  "region": null,
  "version_groups": []
}
```

---

### 25. PokemonGamesAPITest - test_get_pokedex_by_name

**Description:** Test retrieving the Kanto pokedex

**Endpoint:** `/pokedex/kanto`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "kanto"
data["region"]["name"] should match "kanto"
first_entry should be valid
first_entry["pokemon_species"]["name"] should match "bulbasaur"
```

#### Actual Result

```json
From /pokedex/kanto (Response truncated - showing key fields):
{
  "id": 2,
  "name": "kanto",
  "descriptions": [
    {
      "description": "Pokédex régional de Kanto dans Rouge/Bleu/Jaune",
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      }
    },
    {
      "description": "Rot/Blau/Gelb Kanto Dex",
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      }
    },
    "... more items"
  ],
  "is_main_series": true,
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Kanto"
    },
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "Kanto"
    },
    "... more items"
  ],
  "pokemon_entries": [
    {
      "entry_number": 1,
      "pokemon_species": {
        "name": "bulbasaur",
        "url": "https://pokeapi.co/api/v2/pokemon-species/1/"
      }
    },
    {
      "entry_number": 2,
      "pokemon_species": {
        "name": "ivysaur",
        "url": "https://pokeapi.co/api/v2/pokemon-species/2/"
      }
    },
    "... more items"
  ],
  "region": {
    "name": "kanto",
    "url": "https://pokeapi.co/api/v2/region/1/"
  },
  "version_groups": [
    {
      "name": "red-blue",
      "url": "https://pokeapi.co/api/v2/version-group/1/"
    },
    {
      "name": "yellow",
      "url": "https://pokeapi.co/api/v2/version-group/2/"
    },
    "... more items"
  ]
}
```

---

### 26. PokemonGamesAPITest - test_get_version_by_id

**Description:** Test retrieving a version by its ID

**Endpoint:** `/version/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "red"
data["version_group"]["name"] should match "red-blue"
```

#### Actual Result

```json
From /version/1:
{
  "id": 1,
  "name": "red",
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "赤"
    },
    {
      "language": {
        "name": "ko",
        "url": "https://pokeapi.co/api/v2/language/3/"
      },
      "name": "레드"
    },
    {
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "紅"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Rouge"
    },
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "Rot"
    },
    {
      "language": {
        "name": "es",
        "url": "https://pokeapi.co/api/v2/language/7/"
      },
      "name": "Rojo"
    },
    {
      "language": {
        "name": "it",
        "url": "https://pokeapi.co/api/v2/language/8/"
      },
      "name": "Rossa"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Red"
    },
    {
      "language": {
        "name": "zh-Hans",
        "url": "https://pokeapi.co/api/v2/language/12/"
      },
      "name": "紅"
    }
  ],
  "version_group": {
    "name": "red-blue",
    "url": "https://pokeapi.co/api/v2/version-group/1/"
  }
}
```

---

### 27. PokemonGamesAPITest - test_get_version_by_name

**Description:** Test retrieving the Red version

**Endpoint:** `/version/red`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
```

#### Actual Result

```json
From /version/red:
{
  "id": 1,
  "name": "red",
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "赤"
    },
    {
      "language": {
        "name": "ko",
        "url": "https://pokeapi.co/api/v2/language/3/"
      },
      "name": "레드"
    },
    {
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "紅"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Rouge"
    },
    {
      "language": {
        "name": "de",
        "url": "https://pokeapi.co/api/v2/language/6/"
      },
      "name": "Rot"
    },
    {
      "language": {
        "name": "es",
        "url": "https://pokeapi.co/api/v2/language/7/"
      },
      "name": "Rojo"
    },
    {
      "language": {
        "name": "it",
        "url": "https://pokeapi.co/api/v2/language/8/"
      },
      "name": "Rossa"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Red"
    },
    {
      "language": {
        "name": "zh-Hans",
        "url": "https://pokeapi.co/api/v2/language/12/"
      },
      "name": "紅"
    }
  ],
  "version_group": {
    "name": "red-blue",
    "url": "https://pokeapi.co/api/v2/version-group/1/"
  }
}
```

---

### 28. PokemonGamesAPITest - test_get_version_group_by_id

**Description:** Test retrieving a version group by its ID

**Endpoint:** `/version-group/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "red-blue"
data["generation"]["name"] should match "generation-i"
"kanto" should match regions
"red" should match versions
"blue" should match versions
```

#### Actual Result

```json
From /version-group/1:
{
  "generation": {
    "name": "generation-i",
    "url": "https://pokeapi.co/api/v2/generation/1/"
  },
  "id": 1,
  "move_learn_methods": [
    {
      "name": "level-up",
      "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
    },
    {
      "name": "machine",
      "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
    },
    {
      "name": "stadium-surfing-pikachu",
      "url": "https://pokeapi.co/api/v2/move-learn-method/5/"
    }
  ],
  "name": "red-blue",
  "order": 1,
  "pokedexes": [
    {
      "name": "kanto",
      "url": "https://pokeapi.co/api/v2/pokedex/2/"
    }
  ],
  "regions": [
    {
      "name": "kanto",
      "url": "https://pokeapi.co/api/v2/region/1/"
    }
  ],
  "versions": [
    {
      "name": "red",
      "url": "https://pokeapi.co/api/v2/version/1/"
    },
    {
      "name": "blue",
      "url": "https://pokeapi.co/api/v2/version/2/"
    }
  ]
}
```

---

### 29. PokemonGamesAPITest - test_get_version_group_by_name

**Description:** Test retrieving the Red-Blue version group

**Endpoint:** `/version-group/red-blue`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
```

#### Actual Result

```json
From /version-group/red-blue:
{
  "generation": {
    "name": "generation-i",
    "url": "https://pokeapi.co/api/v2/generation/1/"
  },
  "id": 1,
  "move_learn_methods": [
    {
      "name": "level-up",
      "url": "https://pokeapi.co/api/v2/move-learn-method/1/"
    },
    {
      "name": "machine",
      "url": "https://pokeapi.co/api/v2/move-learn-method/4/"
    },
    {
      "name": "stadium-surfing-pikachu",
      "url": "https://pokeapi.co/api/v2/move-learn-method/5/"
    }
  ],
  "name": "red-blue",
  "order": 1,
  "pokedexes": [
    {
      "name": "kanto",
      "url": "https://pokeapi.co/api/v2/pokedex/2/"
    }
  ],
  "regions": [
    {
      "name": "kanto",
      "url": "https://pokeapi.co/api/v2/region/1/"
    }
  ],
  "versions": [
    {
      "name": "red",
      "url": "https://pokeapi.co/api/v2/version/1/"
    },
    {
      "name": "blue",
      "url": "https://pokeapi.co/api/v2/version/2/"
    }
  ]
}
```

---

### 30. PokemonGamesAPITest - test_pagination

**Description:** Test API pagination by getting all generations

**Endpoint:** `/generation`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"count" should match data
"results" should match data
len(data["results"] should be valid
```

#### Actual Result

```json
From /generation:
{
  "count": 9,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "generation-i",
      "url": "https://pokeapi.co/api/v2/generation/1/"
    },
    {
      "name": "generation-ii",
      "url": "https://pokeapi.co/api/v2/generation/2/"
    },
    {
      "name": "generation-iii",
      "url": "https://pokeapi.co/api/v2/generation/3/"
    },
    {
      "name": "generation-iv",
      "url": "https://pokeapi.co/api/v2/generation/4/"
    },
    {
      "name": "generation-v",
      "url": "https://pokeapi.co/api/v2/generation/5/"
    },
    {
      "name": "generation-vi",
      "url": "https://pokeapi.co/api/v2/generation/6/"
    },
    {
      "name": "generation-vii",
      "url": "https://pokeapi.co/api/v2/generation/7/"
    },
    {
      "name": "generation-viii",
      "url": "https://pokeapi.co/api/v2/generation/8/"
    },
    {
      "name": "generation-ix",
      "url": "https://pokeapi.co/api/v2/generation/9/"
    }
  ]
}
```

---

### 31. PokemonItemAPITest - test_error_handling

**Description:** Test API error handling with invalid resource ID

**Endpoint:** `/item/error`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 404
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 32. PokemonItemAPITest - test_get_item_attribute_by_id

**Description:** Test retrieving an item attribute by its ID

**Endpoint:** `/item-attribute/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "countable"
"master-ball" should match items
```

#### Actual Result

```json
From /item-attribute/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "countable",
  "descriptions": [
    {
      "description": "Has a count in the bag",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "items": [
    {
      "name": "master-ball",
      "url": "https://pokeapi.co/api/v2/item/1/"
    },
    {
      "name": "ultra-ball",
      "url": "https://pokeapi.co/api/v2/item/2/"
    },
    "... more items"
  ],
  "names": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Countable"
    }
  ]
}
```

---

### 33. PokemonItemAPITest - test_get_item_attribute_by_name

**Description:** Test retrieving an item attribute by name

**Endpoint:** `/item-attribute/countable`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
```

#### Actual Result

```json
From /item-attribute/countable (Response truncated - showing key fields):
{
  "id": 1,
  "name": "countable",
  "descriptions": [
    {
      "description": "Has a count in the bag",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "items": [
    {
      "name": "master-ball",
      "url": "https://pokeapi.co/api/v2/item/1/"
    },
    {
      "name": "ultra-ball",
      "url": "https://pokeapi.co/api/v2/item/2/"
    },
    "... more items"
  ],
  "names": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Countable"
    }
  ]
}
```

---

### 34. PokemonItemAPITest - test_get_item_by_name

**Description:** Test retrieving an item by its name

**Endpoint:** `/item/master-ball`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
```

#### Actual Result

```json
From /item/master-ball (Response truncated - showing key fields):
{
  "id": 1,
  "name": "master-ball",
  "attributes": [
    {
      "name": "countable",
      "url": "https://pokeapi.co/api/v2/item-attribute/1/"
    },
    {
      "name": "consumable",
      "url": "https://pokeapi.co/api/v2/item-attribute/2/"
    },
    "... more items"
  ],
  "baby_trigger_for": null,
  "category": {
    "name": "standard-balls",
    "url": "https://pokeapi.co/api/v2/item-category/34/"
  },
  "cost": 0,
  "effect_entries": [
    {
      "effect": "Used in battle\n:   Catches a wild Pokémon without fail.\n\n    If used in a trainer battle, nothing happens and the ball is lost.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "short_effect": "Catches a wild Pokémon every time."
    }
  ],
  "flavor_text_entries": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "text": "The best BALL that\ncatches a POKéMON\nwithout fail.",
      "version_group": {
        "name": "ruby-sapphire",
        "url": "https://pokeapi.co/api/v2/version-group/5/"
      }
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "text": "The best BALL that\ncatches a POKéMON\nwithout fail.",
      "version_group": {
        "name": "emerald",
        "url": "https://pokeapi.co/api/v2/version-group/6/"
      }
    },
    "... more items"
  ],
  "fling_effect": null,
  "fling_power": null,
  "game_indices": [
    {
      "game_index": 1,
      "generation": {
        "name": "generation-iii",
        "url": "https://pokeapi.co/api/v2/generation/3/"
      }
    },
    {
      "game_index": 1,
      "generation": {
        "name": "generation-iv",
        "url": "https://pokeapi.co/api/v2/generation/4/"
      }
    },
    "... more items"
  ],
  "held_by_pokemon": []
}
```

---

### 35. PokemonItemAPITest - test_get_item_category_by_id

**Description:** Test retrieving an item category by its ID

**Endpoint:** `/item-category/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "stat-boosts"
data["pocket"]["name"] should match "battle"
```

#### Actual Result

```json
From /item-category/1:
{
  "id": 1,
  "items": [
    {
      "name": "guard-spec",
      "url": "https://pokeapi.co/api/v2/item/55/"
    },
    {
      "name": "dire-hit",
      "url": "https://pokeapi.co/api/v2/item/56/"
    },
    {
      "name": "x-attack",
      "url": "https://pokeapi.co/api/v2/item/57/"
    },
    {
      "name": "x-defense",
      "url": "https://pokeapi.co/api/v2/item/58/"
    },
    {
      "name": "x-speed",
      "url": "https://pokeapi.co/api/v2/item/59/"
    },
    {
      "name": "x-accuracy",
      "url": "https://pokeapi.co/api/v2/item/60/"
    },
    {
      "name": "x-sp-atk",
      "url": "https://pokeapi.co/api/v2/item/61/"
    },
    {
      "name": "x-sp-def",
      "url": "https://pokeapi.co/api/v2/item/62/"
    },
    {
      "name": "max-mushrooms",
      "url": "https://pokeapi.co/api/v2/item/1631/"
    }
  ],
  "name": "stat-boosts",
  "names": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Stat boosts"
    }
  ],
  "pocket": {
    "name": "battle",
    "url": "https://pokeapi.co/api/v2/item-pocket/7/"
  }
}
```

---

### 36. PokemonItemAPITest - test_get_item_category_by_name

**Description:** Test retrieving an item category by name

**Endpoint:** `/item-category/standard-balls`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"master-ball" should match items
```

#### Actual Result

```json
From /item-category/standard-balls (Response truncated - showing key fields):
{
  "id": 34,
  "name": "standard-balls",
  "items": [
    {
      "name": "master-ball",
      "url": "https://pokeapi.co/api/v2/item/1/"
    },
    {
      "name": "ultra-ball",
      "url": "https://pokeapi.co/api/v2/item/2/"
    },
    "... more items"
  ],
  "names": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Standard balls"
    }
  ],
  "pocket": {
    "name": "pokeballs",
    "url": "https://pokeapi.co/api/v2/item-pocket/3/"
  }
}
```

---

### 37. PokemonItemAPITest - test_get_item_fling_effect_by_id

**Description:** Test retrieving an item fling effect by its ID

**Endpoint:** `/item-fling-effect/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "badly-poison"
any("poisons" in entry["effect"] for entry in effect_entries should be valid
```

#### Actual Result

```json
From /item-fling-effect/1:
{
  "effect_entries": [
    {
      "effect": "Badly poisons the target.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "id": 1,
  "items": [
    {
      "name": "toxic-orb",
      "url": "https://pokeapi.co/api/v2/item/249/"
    }
  ],
  "name": "badly-poison"
}
```

---

### 38. PokemonItemAPITest - test_get_item_fling_effect_by_name

**Description:** Test retrieving an item fling effect by name

**Endpoint:** `/item-fling-effect/flinch`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
len(data["items"] should be valid
```

#### Actual Result

```json
From /item-fling-effect/flinch:
{
  "effect_entries": [
    {
      "effect": "Target will flinch if it has not yet gone this turn.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      }
    }
  ],
  "id": 7,
  "items": [
    {
      "name": "kings-rock",
      "url": "https://pokeapi.co/api/v2/item/198/"
    },
    {
      "name": "razor-fang",
      "url": "https://pokeapi.co/api/v2/item/304/"
    }
  ],
  "name": "flinch"
}
```

---

### 39. PokemonItemAPITest - test_get_item_pocket_by_id

**Description:** Test retrieving an item pocket by its ID

**Endpoint:** `/item-pocket/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["name"] should match "misc"
"collectibles" should match categories
```

#### Actual Result

```json
From /item-pocket/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "misc",
  "categories": [
    {
      "name": "collectibles",
      "url": "https://pokeapi.co/api/v2/item-category/9/"
    },
    {
      "name": "evolution",
      "url": "https://pokeapi.co/api/v2/item-category/10/"
    },
    "... more items"
  ],
  "names": [
    {
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "道具"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Objets"
    },
    "... more items"
  ]
}
```

---

### 40. PokemonItemAPITest - test_get_item_pocket_by_name

**Description:** Test retrieving an item pocket by name

**Endpoint:** `/item-pocket/battle`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"stat-boosts" should match categories
```

#### Actual Result

```json
From /item-pocket/battle:
{
  "categories": [
    {
      "name": "stat-boosts",
      "url": "https://pokeapi.co/api/v2/item-category/1/"
    },
    {
      "name": "flutes",
      "url": "https://pokeapi.co/api/v2/item-category/38/"
    },
    {
      "name": "miracle-shooter",
      "url": "https://pokeapi.co/api/v2/item-category/43/"
    }
  ],
  "id": 7,
  "name": "battle",
  "names": [
    {
      "language": {
        "name": "zh-Hant",
        "url": "https://pokeapi.co/api/v2/language/4/"
      },
      "name": "戰鬥道具"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Objets de combat"
    },
    {
      "language": {
        "name": "es",
        "url": "https://pokeapi.co/api/v2/language/7/"
      },
      "name": "Objetos de combate"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Battle Items"
    },
    {
      "language": {
        "name": "zh-Hans",
        "url": "https://pokeapi.co/api/v2/language/12/"
      },
      "name": "战斗道具"
    }
  ]
}
```

---

### 41. PokemonItemAPITest - test_item_pagination

**Description:** Test item API pagination

**Endpoint:** `/item?limit=20&offset=0`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"count" should match data
"results" should match data
len(data["results"] should be valid
"master-ball" should match items
```

#### Actual Result

```json
From /item?limit=20&offset=0:
{
  "count": 2180,
  "next": "https://pokeapi.co/api/v2/item?offset=20&limit=20",
  "previous": null,
  "results": [
    {
      "name": "master-ball",
      "url": "https://pokeapi.co/api/v2/item/1/"
    },
    {
      "name": "ultra-ball",
      "url": "https://pokeapi.co/api/v2/item/2/"
    },
    {
      "name": "great-ball",
      "url": "https://pokeapi.co/api/v2/item/3/"
    },
    {
      "name": "poke-ball",
      "url": "https://pokeapi.co/api/v2/item/4/"
    },
    {
      "name": "safari-ball",
      "url": "https://pokeapi.co/api/v2/item/5/"
    },
    {
      "name": "net-ball",
      "url": "https://pokeapi.co/api/v2/item/6/"
    },
    {
      "name": "dive-ball",
      "url": "https://pokeapi.co/api/v2/item/7/"
    },
    {
      "name": "nest-ball",
      "url": "https://pokeapi.co/api/v2/item/8/"
    },
    {
      "name": "repeat-ball",
      "url": "https://pokeapi.co/api/v2/item/9/"
    },
    {
      "name": "timer-ball",
      "url": "https://pokeapi.co/api/v2/item/10/"
    },
    {
      "name": "luxury-ball",
      "url": "https://pokeapi.co/api/v2/item/11/"
    },
    {
      "name": "premier-ball",
      "url": "https://pokeapi.co/api/v2/item/12/"
    },
    {
      "name": "dusk-ball",
      "url": "https://pokeapi.co/api/v2/item/13/"
    },
    {
      "name": "heal-ball",
      "url": "https://pokeapi.co/api/v2/item/14/"
    },
    {
      "name": "quick-ball",
      "url": "https://pokeapi.co/api/v2/item/15/"
    },
    {
      "name": "cherish-ball",
      "url": "https://pokeapi.co/api/v2/item/16/"
    },
    {
      "name": "potion",
      "url": "https://pokeapi.co/api/v2/item/17/"
    },
    {
      "name": "antidote",
      "url": "https://pokeapi.co/api/v2/item/18/"
    },
    {
      "name": "burn-heal",
      "url": "https://pokeapi.co/api/v2/item/19/"
    },
    {
      "name": "ice-heal",
      "url": "https://pokeapi.co/api/v2/item/20/"
    }
  ]
}
```

---

### 42. PokemonItemAPITest - test_related_item_endpoints

**Description:** Test relationships between item-related endpoints

**Endpoint:** `/item/relationships`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
category_response.status_code should match 200
pocket_response.status_code should match 200
attribute_response.status_code should match 200
```

#### Actual Result

```json
From /item/master-ball (Response truncated - showing key fields):
{
  "id": 1,
  "name": "master-ball",
  "attributes": [
    {
      "name": "countable",
      "url": "https://pokeapi.co/api/v2/item-attribute/1/"
    },
    {
      "name": "consumable",
      "url": "https://pokeapi.co/api/v2/item-attribute/2/"
    },
    "... more items"
  ],
  "baby_trigger_for": null,
  "category": {
    "name": "standard-balls",
    "url": "https://pokeapi.co/api/v2/item-category/34/"
  },
  "cost": 0,
  "effect_entries": [
    {
      "effect": "Used in battle\n:   Catches a wild Pokémon without fail.\n\n    If used in a trainer battle, nothing happens and the ball is lost.",
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "short_effect": "Catches a wild Pokémon every time."
    }
  ],
  "flavor_text_entries": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "text": "The best BALL that\ncatches a POKéMON\nwithout fail.",
      "version_group": {
        "name": "ruby-sapphire",
        "url": "https://pokeapi.co/api/v2/version-group/5/"
      }
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "text": "The best BALL that\ncatches a POKéMON\nwithout fail.",
      "version_group": {
        "name": "emerald",
        "url": "https://pokeapi.co/api/v2/version-group/6/"
      }
    },
    "... more items"
  ],
  "fling_effect": null,
  "fling_power": null,
  "game_indices": [
    {
      "game_index": 1,
      "generation": {
        "name": "generation-iii",
        "url": "https://pokeapi.co/api/v2/generation/3/"
      }
    },
    {
      "game_index": 1,
      "generation": {
        "name": "generation-iv",
        "url": "https://pokeapi.co/api/v2/generation/4/"
      }
    },
    "... more items"
  ],
  "held_by_pokemon": []
}

Also accessed: /item-category/34/, /item-pocket/3/, /item-attribute/1/
```

---

### 43. PokemonLocationAPITest - test_error_handling

**Description:** Test API error handling with invalid resource ID

**Endpoint:** `/location/error`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 404
```

#### Actual Result

```json
No API responses were captured for this test. This might indicate:
1. The test doesn't make API calls
2. The response wasn't JSON
3. All requests failed with non-200 status codes
```

---

### 44. PokemonLocationAPITest - test_get_location_area_by_id

**Description:** Test retrieving a location area by its ID

**Endpoint:** `/location-area/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "canalave-city-area"
data["location"]["name"] should match "canalave-city"
len(data["pokemon_encounters"] should be valid
pokemon_found should match "Tentacool not found in the encounter list"
```

#### Actual Result

```json
From /location-area/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "canalave-city-area",
  "encounter_method_rates": [
    {
      "encounter_method": {
        "name": "old-rod",
        "url": "https://pokeapi.co/api/v2/encounter-method/2/"
      },
      "version_details": [
        {
          "rate": 25,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "rate": 25,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "rate": 25,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    {
      "encounter_method": {
        "name": "good-rod",
        "url": "https://pokeapi.co/api/v2/encounter-method/3/"
      },
      "version_details": [
        {
          "rate": 50,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "rate": 50,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "rate": 50,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    "... more items"
  ],
  "game_index": 1,
  "location": {
    "name": "canalave-city",
    "url": "https://pokeapi.co/api/v2/location/1/"
  },
  "names": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Canalave City"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Joliberges"
    }
  ],
  "pokemon_encounters": [
    {
      "pokemon": {
        "name": "tentacool",
        "url": "https://pokeapi.co/api/v2/pokemon/72/"
      },
      "version_details": [
        {
          "encounter_details": [
            {
              "chance": 60,
              "condition_values": [],
              "max_level": 30,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 60,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 60,
              "condition_values": [],
              "max_level": 30,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 60,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 60,
              "condition_values": [],
              "max_level": 30,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 60,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    {
      "pokemon": {
        "name": "tentacruel",
        "url": "https://pokeapi.co/api/v2/pokemon/73/"
      },
      "version_details": [
        {
          "encounter_details": [
            {
              "chance": 5,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 5,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 5,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 5,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 5,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            },
            {
              "chance": 4,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 9,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    "... more items"
  ]
}
```

---

### 45. PokemonLocationAPITest - test_get_location_area_by_name

**Description:** Test retrieving a location area by name

**Endpoint:** `/location-area/canalave-city-area`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
len(data["encounter_method_rates"] should be valid
"encounter_method" should match rate
"version_details" should match rate
```

#### Actual Result

```json
From /location-area/canalave-city-area (Response truncated - showing key fields):
{
  "id": 1,
  "name": "canalave-city-area",
  "encounter_method_rates": [
    {
      "encounter_method": {
        "name": "old-rod",
        "url": "https://pokeapi.co/api/v2/encounter-method/2/"
      },
      "version_details": [
        {
          "rate": 25,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "rate": 25,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "rate": 25,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    {
      "encounter_method": {
        "name": "good-rod",
        "url": "https://pokeapi.co/api/v2/encounter-method/3/"
      },
      "version_details": [
        {
          "rate": 50,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "rate": 50,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "rate": 50,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    "... more items"
  ],
  "game_index": 1,
  "location": {
    "name": "canalave-city",
    "url": "https://pokeapi.co/api/v2/location/1/"
  },
  "names": [
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Canalave City"
    },
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Joliberges"
    }
  ],
  "pokemon_encounters": [
    {
      "pokemon": {
        "name": "tentacool",
        "url": "https://pokeapi.co/api/v2/pokemon/72/"
      },
      "version_details": [
        {
          "encounter_details": [
            {
              "chance": 60,
              "condition_values": [],
              "max_level": 30,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 60,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 60,
              "condition_values": [],
              "max_level": 30,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 60,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 60,
              "condition_values": [],
              "max_level": 30,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 60,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    {
      "pokemon": {
        "name": "tentacruel",
        "url": "https://pokeapi.co/api/v2/pokemon/73/"
      },
      "version_details": [
        {
          "encounter_details": [
            {
              "chance": 5,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 5,
          "version": {
            "name": "diamond",
            "url": "https://pokeapi.co/api/v2/version/12/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 5,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 5,
          "version": {
            "name": "pearl",
            "url": "https://pokeapi.co/api/v2/version/13/"
          }
        },
        {
          "encounter_details": [
            {
              "chance": 5,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            },
            {
              "chance": 4,
              "condition_values": [],
              "max_level": 40,
              "method": {
                "name": "surf",
                "url": "https://pokeapi.co/api/v2/encounter-method/5/"
              },
              "min_level": 20
            }
          ],
          "max_chance": 9,
          "version": {
            "name": "platinum",
            "url": "https://pokeapi.co/api/v2/version/14/"
          }
        }
      ]
    },
    "... more items"
  ]
}
```

---

### 46. PokemonLocationAPITest - test_get_location_by_id

**Description:** Test retrieving a location by its ID

**Endpoint:** `/location/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "canalave-city"
data["region"]["name"] should match "sinnoh"
len(data["areas"] should be valid
"canalave-city-area" should match areas
```

#### Actual Result

```json
From /location/1:
{
  "areas": [
    {
      "name": "canalave-city-area",
      "url": "https://pokeapi.co/api/v2/location-area/1/"
    }
  ],
  "game_indices": [
    {
      "game_index": 7,
      "generation": {
        "name": "generation-iv",
        "url": "https://pokeapi.co/api/v2/generation/4/"
      }
    }
  ],
  "id": 1,
  "name": "canalave-city",
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Joliberges"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Canalave City"
    }
  ],
  "region": {
    "name": "sinnoh",
    "url": "https://pokeapi.co/api/v2/region/4/"
  }
}
```

---

### 47. PokemonLocationAPITest - test_get_location_by_name

**Description:** Test retrieving a location by its name

**Endpoint:** `/location/canalave-city`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
any(name["language"]["name"] == "en" for name in names should be valid
len(data["game_indices"] should be valid
"generation" should match index
```

#### Actual Result

```json
From /location/canalave-city:
{
  "areas": [
    {
      "name": "canalave-city-area",
      "url": "https://pokeapi.co/api/v2/location-area/1/"
    }
  ],
  "game_indices": [
    {
      "game_index": 7,
      "generation": {
        "name": "generation-iv",
        "url": "https://pokeapi.co/api/v2/generation/4/"
      }
    }
  ],
  "id": 1,
  "name": "canalave-city",
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Joliberges"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Canalave City"
    }
  ],
  "region": {
    "name": "sinnoh",
    "url": "https://pokeapi.co/api/v2/region/4/"
  }
}
```

---

### 48. PokemonLocationAPITest - test_get_pal_park_area_by_id

**Description:** Test retrieving a pal park area by its ID

**Endpoint:** `/pal-park-area/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "forest"
len(data["pokemon_encounters"] should be valid
encounter["base_score"] should match 30
encounter["rate"] should match 50
```

#### Actual Result

```json
From /pal-park-area/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "forest",
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Forêt"
    },
    {
      "language": {
        "name": "es",
        "url": "https://pokeapi.co/api/v2/language/7/"
      },
      "name": "Bosque"
    },
    "... more items"
  ],
  "pokemon_encounters": [
    {
      "base_score": 30,
      "pokemon_species": {
        "name": "caterpie",
        "url": "https://pokeapi.co/api/v2/pokemon-species/10/"
      },
      "rate": 50
    },
    {
      "base_score": 50,
      "pokemon_species": {
        "name": "metapod",
        "url": "https://pokeapi.co/api/v2/pokemon-species/11/"
      },
      "rate": 30
    },
    "... more items"
  ]
}
```

---

### 49. PokemonLocationAPITest - test_get_pal_park_area_by_name

**Description:** Test retrieving a pal park area by name

**Endpoint:** `/pal-park-area/forest`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
any(name["language"]["name"] == "en" for name in names should be valid
```

#### Actual Result

```json
From /pal-park-area/forest (Response truncated - showing key fields):
{
  "id": 1,
  "name": "forest",
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Forêt"
    },
    {
      "language": {
        "name": "es",
        "url": "https://pokeapi.co/api/v2/language/7/"
      },
      "name": "Bosque"
    },
    "... more items"
  ],
  "pokemon_encounters": [
    {
      "base_score": 30,
      "pokemon_species": {
        "name": "caterpie",
        "url": "https://pokeapi.co/api/v2/pokemon-species/10/"
      },
      "rate": 50
    },
    {
      "base_score": 50,
      "pokemon_species": {
        "name": "metapod",
        "url": "https://pokeapi.co/api/v2/pokemon-species/11/"
      },
      "rate": 30
    },
    "... more items"
  ]
}
```

---

### 50. PokemonLocationAPITest - test_get_region_by_id

**Description:** Test retrieving a region by its ID

**Endpoint:** `/region/1`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
data["name"] should match "kanto"
data["main_generation"]["name"] should match "generation-i"
len(data["locations"] should be valid
len(data["pokedexes"] should be valid
"kanto" should match pokedexes
len(data["version_groups"] should be valid
"red-blue" should match version_groups
```

#### Actual Result

```json
From /region/1 (Response truncated - showing key fields):
{
  "id": 1,
  "name": "kanto",
  "locations": [
    {
      "name": "celadon-city",
      "url": "https://pokeapi.co/api/v2/location/67/"
    },
    {
      "name": "cerulean-city",
      "url": "https://pokeapi.co/api/v2/location/68/"
    },
    "... more items"
  ],
  "main_generation": {
    "name": "generation-i",
    "url": "https://pokeapi.co/api/v2/generation/1/"
  },
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "カントー"
    },
    {
      "language": {
        "name": "ko",
        "url": "https://pokeapi.co/api/v2/language/3/"
      },
      "name": "관동"
    },
    "... more items"
  ],
  "pokedexes": [
    {
      "name": "kanto",
      "url": "https://pokeapi.co/api/v2/pokedex/2/"
    },
    {
      "name": "letsgo-kanto",
      "url": "https://pokeapi.co/api/v2/pokedex/26/"
    }
  ],
  "version_groups": [
    {
      "name": "red-blue",
      "url": "https://pokeapi.co/api/v2/version-group/1/"
    },
    {
      "name": "yellow",
      "url": "https://pokeapi.co/api/v2/version-group/2/"
    },
    "... more items"
  ]
}
```

---

### 51. PokemonLocationAPITest - test_get_region_by_name

**Description:** Test retrieving a region by name

**Endpoint:** `/region/kanto`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
data["id"] should match 1
any(name["language"]["name"] == "en" for name in names should be valid
```

#### Actual Result

```json
From /region/kanto (Response truncated - showing key fields):
{
  "id": 1,
  "name": "kanto",
  "locations": [
    {
      "name": "celadon-city",
      "url": "https://pokeapi.co/api/v2/location/67/"
    },
    {
      "name": "cerulean-city",
      "url": "https://pokeapi.co/api/v2/location/68/"
    },
    "... more items"
  ],
  "main_generation": {
    "name": "generation-i",
    "url": "https://pokeapi.co/api/v2/generation/1/"
  },
  "names": [
    {
      "language": {
        "name": "ja-Hrkt",
        "url": "https://pokeapi.co/api/v2/language/1/"
      },
      "name": "カントー"
    },
    {
      "language": {
        "name": "ko",
        "url": "https://pokeapi.co/api/v2/language/3/"
      },
      "name": "관동"
    },
    "... more items"
  ],
  "pokedexes": [
    {
      "name": "kanto",
      "url": "https://pokeapi.co/api/v2/pokedex/2/"
    },
    {
      "name": "letsgo-kanto",
      "url": "https://pokeapi.co/api/v2/pokedex/26/"
    }
  ],
  "version_groups": [
    {
      "name": "red-blue",
      "url": "https://pokeapi.co/api/v2/version-group/1/"
    },
    {
      "name": "yellow",
      "url": "https://pokeapi.co/api/v2/version-group/2/"
    },
    "... more items"
  ]
}
```

---

### 52. PokemonLocationAPITest - test_location_area_pagination

**Description:** Test location area API pagination

**Endpoint:** `/location-area?limit=20&offset=0`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"count" should match data
"results" should match data
len(data["results"] should be valid
"canalave-city-area" should match location_areas
```

#### Actual Result

```json
From /location-area?limit=20&offset=0 (Response truncated - showing key fields):
{
  "count": 1089,
  "next": "https://pokeapi.co/api/v2/location-area?offset=20&limit=20",
  "previous": null,
  "results": [
    {
      "name": "canalave-city-area",
      "url": "https://pokeapi.co/api/v2/location-area/1/"
    },
    {
      "name": "eterna-city-area",
      "url": "https://pokeapi.co/api/v2/location-area/2/"
    },
    "... more items"
  ]
}
```

---

### 53. PokemonLocationAPITest - test_location_pagination

**Description:** Test location API pagination

**Endpoint:** `/location?limit=20&offset=0`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
response.status_code should match 200
"count" should match data
"results" should match data
len(data["results"] should be valid
"canalave-city" should match locations
```

#### Actual Result

```json
From /location?limit=20&offset=0 (Response truncated - showing key fields):
{
  "count": 1039,
  "next": "https://pokeapi.co/api/v2/location?offset=20&limit=20",
  "previous": null,
  "results": [
    {
      "name": "canalave-city",
      "url": "https://pokeapi.co/api/v2/location/1/"
    },
    {
      "name": "eterna-city",
      "url": "https://pokeapi.co/api/v2/location/2/"
    },
    "... more items"
  ]
}
```

---

### 54. PokemonLocationAPITest - test_related_location_endpoints

**Description:** Test relationships between location-related endpoints

**Endpoint:** `/location/relationships`

**Status:** ✅ PASS

#### Expected Result

```
Should return data where:
region_response.status_code should match 200
area_response.status_code should match 200
area_data["location"]["name"] should match "canalave-city"
```

#### Actual Result

```json
From /location/canalave-city:
{
  "areas": [
    {
      "name": "canalave-city-area",
      "url": "https://pokeapi.co/api/v2/location-area/1/"
    }
  ],
  "game_indices": [
    {
      "game_index": 7,
      "generation": {
        "name": "generation-iv",
        "url": "https://pokeapi.co/api/v2/generation/4/"
      }
    }
  ],
  "id": 1,
  "name": "canalave-city",
  "names": [
    {
      "language": {
        "name": "fr",
        "url": "https://pokeapi.co/api/v2/language/5/"
      },
      "name": "Joliberges"
    },
    {
      "language": {
        "name": "en",
        "url": "https://pokeapi.co/api/v2/language/9/"
      },
      "name": "Canalave City"
    }
  ],
  "region": {
    "name": "sinnoh",
    "url": "https://pokeapi.co/api/v2/region/4/"
  }
}

Also accessed: /region/4/, /location-area/1/
```

---

