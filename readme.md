# Notes 
1. The `PutObject` api defaults to binary/octet stream if you do not specify the content type. To do this, use `--content-type ""`.
2. `aws s3 cp` might be the better option as the command automatically tries to detect and set the correct content type.
3. Rename your main html file to `index.html` for the website to dafault to it.
4. Static website hosting must be enabled in bucket properties to host a website
5. Ensure bucket has the right permissions (including ACL) and policy (json file) to allow public read access.
```{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
    ]
}

## Route 53 (DNS)
1. After creating a hosted zone for your domain, records inform the DNS how you want traffic to be routed for that domain.
2. Records can do the following:
    - Route internet traffic for example.com to the IP address of a host in your data center
    - Route email for that domain (ichiro@example.com) to a mail server (mail.example.com)
3. The name of each record in the hosted zone must end with the name of the hosted zone.

## To enable custom domain name with HTTPS:
1. Obtain a SSL/TLS cert using ACM or any third-party certificate manager.
2. Attach the cert to your cloudfront distribution
3. Update DNS settings
    •	Create a CNAME record pointing your custom domain (e.g., www.example.com) to the CloudFront domain name (e.g., dxxxxxxxxxxxxx.cloudfront.net).
	•	Alternatively, use an Alias record (preferred for Route 53) pointing to the CloudFront distribution.
4. Configure viewer policy
    - In cloudfront, set viewer policy to 
        1. redirect HTTP to HTTPS or,
        2. HTTPS only
Note: An alias record maps your domain to specific AWS resources without needing to know their IP addresses. If you
use s3 bucket to host a website, you need to create an alias record

## Reflection
What aspect of Chunk 1's work did you find the most difficult?
- Configuring Route 53 to point to my cloudfront distribution.
- Understanding DNS configuration and records (including alias records)

Note one or two problems you overcame to get the static site deployed; include the error messages orscreenshots of the issues, and writedown what you did to fix them.
1. Entering the cloudfront distribution domain URL in the browser returned a HTTP 403 access denied message. This is because the default root object was not configured.
To resolve this: Enter default root object as `index.html` in cloudfront distribution general settings

What i did to convert the resources into IaC:
Protect DNS setup from MitM (DNSSEC):