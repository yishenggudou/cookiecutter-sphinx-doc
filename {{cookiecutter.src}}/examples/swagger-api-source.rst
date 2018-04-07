测试从swagger自动生成API SOURCE
==============================


.. http:get:: /users/(int:user_id)/posts/(tag)

   The posts tagged with `tag` that the user (`user_id`) wrote.

   **Example request**:

   .. sourcecode:: http

      GET /users/123/posts/web HTTP/1.1
      Host: example.com
      Accept: application/json, text/javascript

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
        {
          "post_id": 12345,
          "author_id": 123,
          "tags": ["server", "web"],
          "subject": "I tried Nginx"
        },
        {
          "post_id": 12346,
          "author_id": 123,
          "tags": ["html5", "standards", "web"],
          "subject": "We go to HTML 5"
        }
      ]

   :query sort: one of ``hit``, ``created-at``
   :query offset: offset number. default is 0
   :query limit: limit number. default is 30
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :statuscode 200: no error
   :statuscode 404: there's no user


.. http:get:: /odc/v3/databases

   ListAction



   **Example request**:

   .. sourcecode:: http

      GET /odc/v3/databases?session_id=example_value HTTP/1.1
      Host: timger.com.cn
      Accept: application/json,


   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: text/javascript

      [
          {
              "id": 30,
              "name": "string"
          }
      ]




   :query string session_id: session_id query parameter `session_id` is not required
   :reqheader Accept: application/json,



   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: */*,

   :statuscode 401: Unauthorized
   :statuscode 404: Not Found
   :statuscode 403: Forbidden
   :statuscode 200: OK
