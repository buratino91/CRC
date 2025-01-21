# CRC
My attempt at the cloud resume challenge
## Chunk 1 - Building the front end
1. Static website hosted on a S3 bucket
2. Cloudfront CDN integrated with S3 for HTTPS
3. Route 53 for DNS for custom domain name

## Chunk 2 - Building the backend
1. Dynamodb table to store the view count
2. Lambda functions to update the count and retrieve the count
3. Two HTTP APIs created using API gateway to accept requests from the webpage and communicate with the database.

## Chunk 3 - Tying the frontend and backends together
1. Javascript to make the HTTP requests to the API gateway
2. Ensureing CORS is configured properly so that the APIs can be called from the domain
2. Basic HTML modifications to display a counter
3. End-to-end test using cypress

## Architecture
![Alt text](CRC_architecture(1).png)