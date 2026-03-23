# Serverless Visitor API
### API Gateway → Lambda → DynamoDB on AWS

[![AWS](https://img.shields.io/badge/AWS-Serverless-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![API Gateway](https://img.shields.io/badge/Amazon-API%20Gateway-purple?logo=amazon-aws)](https://aws.amazon.com/api-gateway/)
[![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow?logo=aws-lambda)](https://aws.amazon.com/lambda/)
[![DynamoDB](https://img.shields.io/badge/Amazon-DynamoDB-4053D6?logo=amazon-dynamodb)](https://aws.amazon.com/dynamodb/)

---

## Overview

This project implements a fully serverless backend API on AWS. When a client sends a POST request to the endpoint, API Gateway routes it to a Lambda function which generates a unique visitor ID, captures a timestamp, and persists the record to DynamoDB — with no servers to provision or manage.

The architecture is lightweight, infinitely scalable, and costs nothing at rest.

---

## Architecture

![Architecture Diagram](architecture-diagram.png)

```
Client
  │
  ▼
Amazon API Gateway  ──(POST /visit)──▶  AWS Lambda  ──▶  Amazon DynamoDB
                                            │
                                            └── Generates visitor ID + timestamp
                                                Stores record → returns 200 OK
```

---

## Real-World Use Cases

This pattern is widely used in production serverless systems:

| Use Case | Description |
|---|---|
| **Visitor Tracking** | Log unique page visits on a website or app |
| **Event Logging** | Capture user actions or system events |
| **Lightweight APIs** | Backend endpoints without managing servers |
| **Serverless Microservices** | Isolated, independently deployable service units |

AWS automatically handles scaling, availability, and infrastructure — the system scales from zero to millions of requests with no configuration changes.

---

## Services Used

| Service | Role |
|---|---|
| **Amazon API Gateway** | Exposes the HTTP endpoint and routes incoming requests |
| **AWS Lambda** | Processes each request, generates IDs, and writes to DynamoDB |
| **Amazon DynamoDB** | Stores visitor records as NoSQL items |
| **AWS IAM** | Grants Lambda least-privilege access to DynamoDB |

---

## How It Works

1. Client sends a POST request to the API endpoint:
    ```
    POST /visit
    ```
2. **API Gateway** receives and validates the request, then triggers the Lambda function.
3. **Lambda** executes and:
   - Generates a unique `visitor_id`
   - Captures the current `timestamp`
   - Writes the record to DynamoDB
4. **API Gateway** returns a `200 OK` response:
    ```
    Visitor stored successfully
    ```

---

## Lambda Function

Source: [`lambda/lambda_function.py`](lambda/lambda_function.py)

The function uses the AWS SDK (`boto3`) to write directly to DynamoDB using `put_item`, with a UUID for uniqueness and `datetime.utcnow()` for the timestamp.

---

## Project Structure

```
serverless-visitor-api/
│
├── lambda/
│   └── lambda_function.py       # Lambda handler — generates ID, writes to DynamoDB
│
├── architecture-diagram.png     # End-to-end architecture overview
├── README.md
│
└── screenshots/
    ├── 1-dynamodb-table.png     # DynamoDB table configuration
    ├── 2-lambda-function.png    # Lambda function overview
    ├── 3-iam-role.png           # IAM role and attached policies
    ├── 4-lambda-code.png        # Lambda source code in AWS Console
    ├── 5-api-route.png          # API Gateway route definition
    ├── 6-api-stage.png          # API Gateway deployed stage
    ├── 7-api-test.png           # Live API test and response
    └── 8-dynamodb-items.png     # Records stored in DynamoDB after test
```

---

## Screenshots

### 1. DynamoDB Table
*Table created to store visitor records, with `visitor_id` as the partition key.*

![DynamoDB Table](screenshots/1-dynamodb-table.png)

---

### 2. Lambda Function
*Lambda function configured with the correct runtime, handler, and execution role.*

![Lambda Function](screenshots/2-lambda-function.png)

---

### 3. IAM Role Permissions
*IAM role granting Lambda least-privilege access — `PutItem` on the DynamoDB table only.*

![IAM Role](screenshots/3-iam-role.png)

---

### 4. Lambda Code
*Handler logic: generates a UUID, captures a UTC timestamp, and writes to DynamoDB.*

![Lambda Code](screenshots/4-lambda-code.png)

---

### 5. API Gateway Route
*POST `/visit` route defined and integrated with the Lambda function.*

![API Route](screenshots/5-api-route.png)

---

### 6. API Gateway Stage
*API deployed to a live stage with an invokable public endpoint URL.*

![API Stage](screenshots/6-api-stage.png)

---

### 7. API Test
*Live test confirming the endpoint returns `200 OK` and the success message.*

![API Test](screenshots/7-api-test.png)

---

### 8. DynamoDB Records
*Records written to DynamoDB after the API test — visitor ID and timestamp confirmed.*

![DynamoDB Records](screenshots/8-dynamodb-items.png)

---

## Key Concepts Demonstrated

- **Serverless API design** — building a fully functional backend with no infrastructure to manage
- **API Gateway → Lambda integration** — routing HTTP requests to serverless compute
- **DynamoDB data persistence** — writing structured records to a NoSQL table via the AWS SDK
- **IAM least-privilege** — scoping Lambda permissions to only what it needs
- **Event-driven execution** — Lambda runs only when invoked, scaling automatically with demand

---

## Author

**Sergiu Gota**
AWS Certified Solutions Architect – Associate · AWS Cloud Practitioner

[![GitHub](https://img.shields.io/badge/GitHub-sergiugotacloud-181717?logo=github)](https://github.com/sergiugotacloud)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-sergiu--gota--cloud-0A66C2?logo=linkedin)](https://linkedin.com/in/sergiu-gota-cloud)

> Built as part of a cloud portfolio to demonstrate real-world serverless architecture on AWS.
> Feel free to fork, adapt, or reach out with questions.
