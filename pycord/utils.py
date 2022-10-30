# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2021-present VincentRPS
# Copyright (c) 2022-present Pycord Development
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

from typing import Any

from aiohttp import ClientResponse

try:
    import msgspec
except ImportError:
    import json

    msgspec = None

DISCORD_EPOCH: int = 1420070400000


async def _text_or_json(cr: ClientResponse, self) -> str | dict[str, Any]:
    if cr.content_type == 'application/json':
        return await cr.json(encoding='utf-8', loads=self._json_decoder)
    return await cr.text('utf-8')


def loads(data: Any) -> Any:
    return msgspec.json.decode(data.encode()) if msgspec else json.loads(data)


def dumps(data: Any) -> str:
    return msgspec.json.encode(data).decode('utf-8') if msgspec else json.dumps(data)
