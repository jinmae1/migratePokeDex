# Pokemon (endpoint)
# Get https://pokeapi.co/api/v2/pokemon/{id or name}/

from pokebase.loaders import version

class Pokemon:
    def __init__(self, id, name, base_experience, height, is_default, order, weight, abilities, forms, game_indices, held_items, location_area_encounters, moves, sprites, species, stats, types):
        self.id: int = id
        self.name: str = name
        self.base_experience: int = base_experience
        self.height: int = height
        self.is_default: bool = is_default
        self.order: int = order
        self.weight: int = weight
        self.abilities: list = self.get_ability_list(abilities)
        self.forms: list = self.get_form_list(forms)
        self.game_indices: list = game_indices
        self.held_items: list = held_items
        self.location_area_encounters: str = location_area_encounters
        self.moves: list = self.get_move_list(moves) 
        self.sprites: PokemonSprites = self.PokemonSprites(sprites)
        self.species: PokemonSpecies = species
        self.stats: list = self.get_stat_list(stats)
        self.types: list = self.get_type_list(types)

    class PokemonAbility:
        def __init__(self, ability):
            self.is_hidden: bool = ability.is_hidden
            self.slot: int = ability.slot
            self.ability: Ability = ability.ability

    class PokemonType:
        def __init__(self, type_):
            self.slot: int = type_.slot
            self.type: Type = type_.type

    class PokemonHelItem:
        def __init__(self, held_items):
            self.item: Item = held_items.item
            self.version_details: PokemonHeldItemVersion = held_items.version_details

        # inner class
        class PokemonHeldItemVersion:
            def __init__(self, version_details):
                self.version: Version = version_details.version
                self.rarity: int = version_details.rarity

        def get_held_item_list(self, version_details):
            held_item_list: list = list()
            for held_item in version_details:
                held_item_list.append(self.PokemonHeldItemVersion(held_item))
            return held_item_list

    class PokemonMove:
        def __init__(self, move):
            self.move: Move = move.move 
            self.version_group_details: list = self.get_move_version_list(move.version_group_details)

        # inner class
        class PokemonMoveVersion:
            def __init__(self, version_group_details):
                self.move_learn_method: MoveLearnMethod = version_group_details.move_learn_method
                self.version_group: Group = version_group_details.version_group
                self.level_learned_at: int = version_group_details.level_learned_at

        def get_move_version_list(self, version_group_details):
            move_version_list: list = list()
            for move_version in version_group_details:
                move_version_list.append(self.PokemonMoveVersion(move_version))
            return move_version_list
    
    class PokemonStat:
        def __init__(self, stat):
            self.stat: Stat = stat.stat
            self.effort: int = stat.effort
            self.base_stat: int = stat.base_stat

    class PokemonSprites:
        def __init__(self, sprite):
            self.front_default = sprite.front_default
            self.front_shiny = sprite.front_shiny
            self.front_female = sprite.front_female
            self.front_shiny_female = sprite.front_shiny_female
            self.back_default = sprite.back_default
            self.back_shiny = sprite.back_shiny
            self.back_female = sprite.back_female
            self.back_shiny_female = sprite.back_shiny_female

    def get_ability_list(self, abilities: list) -> list:
        ability_list: list = list() 
        for ability in abilities:
            ability_list.append(self.PokemonAbility(ability))
        return ability_list

    def get_type_list(self, types: list) -> list:
        type_list: list = list() 
        for type_ in types:
            type_list.append(self.PokemonType(type_)) 
        return type_list

    def get_held_item_list(self, held_items: list) -> list:
        held_item_list: list = list()
        for held_item in held_items:
            held_item_list.append(self.Poke)

    def get_move_list(self, moves: list) -> list:
        move_list: list = list()
        for move in moves:
            move_list.append(self.PokemonMove(move))
        return move_list

    def get_stat_list(self, stats: list) -> list:
        stat_list: list = list()
        for stat in stats:
            stat_list.append(self.PokemonStat(stat))
        return stat_list

    def get_form_list(self, forms: list) -> list:
        form_list: list = list()
        for form in forms:
            form_list.append(form)
        return form_list

    def get_game_indices_list(self, game_indices: list) -> list:
        game_indices_list: list = list()
        for game_index in game_indices:
            game_indices.append(game_index)
        return game_indices_list