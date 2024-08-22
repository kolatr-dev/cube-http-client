import asyncio

import cube_http
from cube_http.types.v1 import V1LoadRequestQuery


async def main():
    cube = cube_http.AsyncClient(
        {
            "url": "http://localhost:4000/cubejs-api",
            "token": "i9f5e76b519a44b060daa33e78c5de170",
        }
    )

    load_resp = await cube.v1.load(
        {
            "measures": ["tasks.count"],
            "filters": [
                {
                    "or": [
                        {
                            "member": "tasks.status",
                            "operator": "equals",
                            "values": ["Completed"],
                        },
                        {
                            "member": "tasks.priority",
                            "operator": "equals",
                            "values": ["High"],
                        },
                    ]
                }
            ],
        },
    )

    results = load_resp.results

    if results:
        result = results[0]
        print(result.data)

        query = V1LoadRequestQuery.model_validate(result.query)

        sql_resp = await cube.v1.sql(query)
        sql, params = sql_resp.sql.sql
        print(sql)
        print(params)


if __name__ == "__main__":
    asyncio.run(main())
