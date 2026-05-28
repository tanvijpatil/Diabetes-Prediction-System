import bentoml

@bentoml.service
class DiabetesService:

    @bentoml.api
    def predict(self, input_data: dict) -> dict:

        return {
            "prediction": "Not Diabetic"
        }