# Metrics

> Returns the metric values for the specified period.



## OpenAPI

````yaml api.yaml get /metrics
openapi: 3.1.1
info:
  title: Weave API
  version: 1.0.0
  description: API for retrieving Weave metrics.
servers:
  - url: https://app.workweave.ai/api/v1
    description: Production API
security:
  - apiKeyAuth: []
paths:
  /metrics:
    get:
      summary: Metrics
      description: Returns the metric values for the specified period.
      operationId: getMetrics
      parameters:
        - name: metric
          in: query
          required: true
          description: The metrics to retrieve.
          schema:
            type: array
            minItems: 1
            items:
              type: string
              enum:
                - code_output
                - code_output_per_engineer
        - name: start
          in: query
          required: true
          description: >-
            Start date for the metrics period. Cannot be more than one year
            before the end date.
          schema:
            type: string
            format: date-time
            example: '2025-01-01T01:02:03Z'
        - name: end
          in: query
          required: false
          description: >-
            End date for the metrics period. Defaults to today. Cannot be more
            than one year after the start date.
          schema:
            type: string
            format: date-time
            example: '2025-06-01T01:02:03Z'
        - name: granularity
          in: query
          required: false
          description: The granularity of the metrics. Defaults to day.
          schema:
            type: string
            enum:
              - day
              - week
              - month
              - quarter
        - name: timezone
          in: query
          required: false
          description: >
            IANA timezone identifier (e.g., "America/Los_Angeles",
            "Europe/London"). When provided, start and end dates are interpreted
            as midnight in that timezone. Defaults to UTC for backward
            compatibility.
          schema:
            type: string
            example: America/Los_Angeles
      responses:
        '200':
          description: A JSON array of metrics.
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Metric'
              example:
                - date: '2025-01-01'
                  code_output: 12
                  code_output_per_engineer: 1.2
                - date: '2025-01-02'
                  code_output: 15
                  code_output_per_engineer: 1.5
                - date: '2025-01-03'
                  code_output: 18
                  code_output_per_engineer: 1.8
        '400':
          description: Invalid input
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '429':
          description: Rate limit exceeded
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Metric:
      type: object
      required:
        - date
      properties:
        date:
          type: string
          format: date
          description: The start date for this metric period, in UTC.
          example: '2025-01-01'
        code_output:
          type: number
          minimum: 0
          description: Total code output for this period, if requested.
          example: 12
        code_output_per_engineer:
          type: number
          minimum: 0
          description: Average code output per engineer for this period, if requested.
          example: 1.2
    Error:
      type: object
      required:
        - message
      properties:
        message:
          type: string
          description: Error message describing what went wrong
        description:
          type: string
          description: Additional information about the error.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key for authentication.

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt