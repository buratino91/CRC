# CRC
My attempt at the cloud resume challenge
## Chunk 1 - Building the front end
1. Static website hosted on a S3 bucket
2. Cloudfront CDN integrated with S3 for HTTPS
3. Route 53 for DNS for custom domain name

### Reflection
What aspect of Chunk 1's work did you find the most difficult?
- Configuring Route 53 to point to my cloudfront distribution.
- Understanding DNS configuration and records (including alias records)

Note one or two problems you overcame to get the static site deployed; include the error messages orscreenshots of the issues, and writedown what you did to fix them.
1. Entering the cloudfront distribution domain URL in the browser returned a HTTP 403 access denied message. This is because the default root object was not configured.
To resolve this: Enter default root object as `index.html` in cloudfront distribution general settings

What i did to convert the resources into IaC:
Protect DNS setup from MitM (DNSSEC):

## Chunk 2 - Building the backend
1. Dynamodb table to store the view count
2. Lambda functions to update the count and retrieve the count
3. Two HTTP APIs created using API gateway to accept requests from the webpage and communicate with the database.

### Reflection
**What aspect of Chunk 2's work did you find the most difficult?**
1. Writing the lambda function to update an item into my dynamodb table
2. Learning how to use the update_item API for dynamodb.
    a. Understanding the syntax for UpdateExpression’, ‘ExpressionAttributeNames’ and ‘ExpressionAttributeValues’

**Note one or two problems you overcame to get the cloud function talking to your database; include the error messages or screenshots of the issues, and write down what you did to fix them**
1. “Error” : “body” when using the POST method in postman to update the viewer counter.
![Alt text](<message Error updating value,.png>)
Have to enter the required parameters in the 'body' section since this is a POST request
2. Test event format was wrongly structured. This resulted in a failure when testing the lambda function. To resolve this, ensure that the event[‘body’] is received as a string and must be escaped (for HTTP API). This is because:
    - When an HTTP request is made to API Gateway, the request body is always transmitted as a string, since HTTP can only transmit text.
    - API Gateway then takes this string and places it into the body field of the Lambda event, maintaining its string format.
    - If the original request body was JSON, it remains a JSON string inside the body field, which will result in an error. JSON  strings containing quotes must escape those quotes to prevent them from prematurely terminating the string.
    - Without escaping, "body": "{"count": "10"}" would be invalid JSON because the quotes around count would break the JSON syntax
Correct syntax: 
![Alt text](<Pasted Graphic 3.png>)