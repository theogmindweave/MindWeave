# Rate limits

The Weave API has a rate limit of **100 requests per hour per organization**.

If you exceed this limit, you will receive a `429` status code with a JSON error response.

## Rate limit headers

Every API response includes headers to help you track your rate limit usage:

* `X-RateLimit-Limit`: The maximum number of requests allowed per hour (100)
* `X-RateLimit-Remaining`: The number of requests remaining in the current window
* `X-RateLimit-Reset`: Unix timestamp when the rate limit window resets
* `X-RateLimit-Used`: The number of requests used in the current window
* `Retry-After`: When rate limited, the number of seconds to wait before retrying (only present on 429 responses)

## Handling rate limits

When you receive a `429 Too Many Requests` response:

1. Check the `Retry-After` header to see how long to wait
2. Wait for the specified duration
3. Retry your request after the wait period

## Best practices

* Cache responses when possible to reduce API calls
* Implement rate limit handling in your client code


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.workweave.ai/llms.txt