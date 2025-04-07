import json

class MealyMachine:
    def __init__(self, states, transitions, initial_state, input_sequence):
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.input_sequence = str(input_sequence)
    
    def run_machine(self):
        current_state = self.initial_state
        path = [current_state]
        output_str = ""

        for char in self.input_sequence:
            if char not in self.transitions[current_state]:
                # Menghentikan loop jika input tidak valid
                break
            transitioning = self.transitions[current_state][char]
            current_state = transitioning["next_state"]  # Akses state berikutnya
            path.append(current_state)  # Tambahkan state saat ini setelah transisi
            output_str += transitioning["output"]  # Tambahkan output dari transisi
        return path, output_str
    
    def print_result(self):
        path, output_str = self.run_machine()
        pathofinput = "Path: " + " → ".join(path)
        print(pathofinput)
        print("Output:", output_str)

class MealyMachine_json_reader:
    def convert_json_to_dict(self, file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data

    def convert_dict_to_machine_class(self, data):
        return MealyMachine(
            states=data['states'],
            transitions=data['transitions'],
            initial_state=data['initial_state'],
            input_sequence=data['input_sequence']
        )
    
    def convert_data_to_dict(self, machine):
        data = {
            "states": machine.states,
            "transitions": machine.transitions,
            "initial_state": machine.initial_state,
            "input_sequence": machine.input_sequence
        }
        return data

    def convert_dict_to_json(self, data, file_path):
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    reader = MealyMachine_json_reader()
    json_data = reader.convert_json_to_dict("input1.json")
    machine = reader.convert_dict_to_machine_class(json_data)
    machine.print_result()
