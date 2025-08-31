import pickle
import warnings
warnings.filterwarnings("ignore")


class Model:
    def __init__(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                data = pickle.load(f)

            self.model = data['model']
            self.actions = data['actions']
            print("Model and actions loaded successfully.")
        except FileNotFoundError:
            print("Model file not found. Please ensure the model is trained and saved correctly.")
            self.model = None
            self.actions = None


    def predict(self, input_data):
        # p1_health	
        # p1_jumping	
        # p1_crouching	
        # p1_is_move	
        # p2_health	
        # p2_jumping	
        # p2_crouching	
        # p2_is_move	
        # distance	
        data = []
        data.append(input_data['p1_health'])
        if input_data['p1_jumping'] == False:
            data.append(0)
        else:
            data.append(1)
        if input_data['p1_crouching'] == False:
            data.append(0)
        else:
            data.append(1)
        if input_data['p1_is_move'] == False:   
            data.append(0)
        else:
            data.append(1)

        data.append(input_data['p2_health'])
        if input_data['p2_jumping'] == False:
            data.append(0)
        else:
            data.append(1)
        if input_data['p2_crouching'] == False:
            data.append(0)
        else:
            data.append(1)
        if input_data['p2_is_move'] == False:   
            data.append(0)
        else:
            data.append(1)

        data.append(input_data['distance'])
        data = [data]

        pred = self.model.predict(data)
        pred = pred[0]
        for i in self.actions.keys():
            if self.actions[i] == pred:
                return i
        print("Prediction failed. Please check the input data and model.")
        return None