from flask import Response


class BaseResponse(Response):
    def __init__(
        self, code: int, message: str, data: object, **kwargs
    ):
        self.resp_code = code
        self.resp_data = data
        self.resp_message = message

        kwargs.pop("response", None)

        super().__init__(
            response=self.__make_response(),
            mimetype=kwargs.pop("mimetype", None) or "application/json",
            **kwargs,
        )

    def __make_response(self):
        from app.models.vo import BaseResponseData
        return BaseResponseData(
            code=self.resp_code, data=self.resp_data, message=self.resp_message,
        ).json()


class CommonResponse(BaseResponse):
    DEFAULT_MSG = "请求成功"

    def __init__(
        self,
        code: int = 200,
        msg: str = DEFAULT_MSG,
        data: object = None,
        **kwargs,
    ):
        super().__init__(code=code, message=msg, data=data, **kwargs)
