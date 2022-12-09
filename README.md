A web application that predicts the dollar amount, a person is expected to pay as premium for thier health insurance taking into account factors like thier region of stay, marriage status, smoker or not, number of childer  For choosing the most accurate model, the parent dataset went through various treatments to yield several derived datasets. These treatments included label encoding of categorical variables, handling missing values using different techniques, oversampling of data, outlier treatments, etc. All datasets with a combined 5000+ entries were feature-engineered using python and then trained as ML Classification Models using Google Cloud Platform's Vertex AI. Next, the most accurate model was chosen to be used for prediction in the web application.  The final prediction is done by passing the data input by the user as a JSON file with the help of a cloud function using POST API to the chosen ML classification model. The model returns the dollar amount a person should be expecting to pay.
