import cc_dat_utils
import cc_classes
import json


# Part 3
# Load your custom JSON file
# Convert JSON data to CCLevelPack
# Save converted data to DAT file

def json_to_cclevelpack(json_data):
    cc_level_pack = cc_classes.CCLevelPack()

    for count, level in enumerate(json_data["levels"], start=1):
        level_number = count
        time = level["time"]
        num_chips = level["num_chips"]
        cc_map_title_field = level["optional_fields"]["CCMapTitleField"]
        cc_map_hint_field = level["optional_fields"]["CCMapHintField"]
        # cc_encoded_password_field = level["optional_fields"]["CCEncodedPasswordField"]
        
        password = str(level["optional_fields"]["CCEncodedPasswordField"])
        part1 = password[:3]
        part2 = password[3:6]
        part3 = password[6:9]
        part4 = password[9:]
        
        cc_encoded_password_field = [int(part1), int(part2), int(part3), int(part4)]

        cc_monster_movement_field = level["optional_fields"]["CCMonsterMovementField"]
        cc_trap_controls_field = level["optional_fields"]["CCTrapControlsField"]
        cc_cloning_machine_controls_field = level["optional_fields"]["CCCloningMachineControlsField"]
        upper_layer = level["upper_layer"]
        #lower_layer = level["lower_layer"]

        cc_level = cc_classes.CCLevel()
        cc_level.level_number = level_number
        cc_level.time = time
        cc_level.num_chips = num_chips
        cc_level.upper_layer = upper_layer
        #cc_level.lower_layer = lower_layer
        

        cc_level.add_field(cc_classes.CCMapTitleField(cc_map_title_field))
        cc_level.add_field(cc_classes.CCMapHintField(cc_map_hint_field))
        cc_level.add_field(cc_classes.CCEncodedPasswordField(cc_encoded_password_field))

        # if more than one monster, put this in a for loop and instantiate each monster
        monster_coords = cc_classes.CCCoordinate(cc_monster_movement_field["x"], cc_monster_movement_field["y"])
        monster_list = [monster_coords]
        cc_level.add_field(cc_classes.CCMonsterMovementField(monster_list))

        # same with traps and cloning machine
        trap_control_b_coord = cc_classes.CCCoordinate(cc_trap_controls_field["bx"], cc_trap_controls_field["by"])
        trap_control_t_coord = cc_classes.CCCoordinate(cc_trap_controls_field["tx"], cc_trap_controls_field["ty"])
        trap_control = cc_classes.CCTrapControl(trap_control_b_coord.x, trap_control_b_coord.y, trap_control_t_coord.x,
                                                trap_control_t_coord.y)
        trap_list = [trap_control]
        cc_level.add_field(cc_classes.CCTrapControlsField(trap_list))

        clone_control_b_coord = cc_classes.CCCoordinate(cc_cloning_machine_controls_field["bx"],
                                                        cc_cloning_machine_controls_field["by"])
        clone_control_t_coord = cc_classes.CCCoordinate(cc_cloning_machine_controls_field["tx"],
                                                        cc_cloning_machine_controls_field["ty"])
        clone_control = cc_classes.CCCloningMachineControl(clone_control_b_coord.x, clone_control_b_coord.y,
                                                           clone_control_t_coord.x, clone_control_t_coord.y)
        clone_list = [clone_control]
        cc_level.add_field(cc_classes.CCCloningMachineControlsField(clone_list))

        cc_level_pack.add_level(cc_level)

    return cc_level_pack


# input_json_file = "data/ichhaya_cc1.json"
input_json_file = "data/ichhaya_cc_level_pack.json"

with open(input_json_file, "r") as reader:
    game_json_data = json.load(reader)

cc_level_pack_obj = json_to_cclevelpack(game_json_data)

# cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack_obj, "C:/Users/ibrah/OneDrive/Documents/Masters/Programming for Game Designers/Tile World/sets/ichhaya_cc1.dat")
# cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack_obj, "data/ichhaya_cc1.dat")

# cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack_obj, "C:/Users/ibrah/OneDrive/Documents/Masters/Programming for Game Designers/Tile World/sets/ichhaya_cc_level_pack.dat")
cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack_obj, "data/ichhaya_cc_level_pack.dat")