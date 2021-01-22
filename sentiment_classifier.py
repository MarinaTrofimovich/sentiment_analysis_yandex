import joblib
class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load('sent_class.pkl')
        self.classes_dict = {0: 'Negative', 1: 'Positive', -1: 'Error of prediction'}
        
    def predict_text(self, text):
        try:
            lst = []
            lst.append(text)
            return self.model.predict(lst)
        except:
            print("Error of prediction")
            return -1
        
    def predict_list(self, list_of_texts):
        try:
            return self.model.predict(list_of_texts)
        except:
            print("Error of prediction")
            return -1
        
    def get_prediction_message(self, text):
        print(text)
        prediction = self.predict_text(text)
        print(prediction)
        return self.classes_dict[int(prediction[0])]