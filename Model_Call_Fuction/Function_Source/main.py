from google.cloud import aiplatform


def insurance_predictor(request):
    req = request.get_json()
    project = req['projectid']
    location = "us-central1"
    instances = req['instance_dict']['instances']
    endpoint = req['endpoint_id']
    aiplatform.init(project=project, location=location)
    endpoint = aiplatform.Endpoint(endpoint)
    prediction = endpoint.predict(instances=instances)
    print(prediction)
    return (str(int(prediction.predictions)))