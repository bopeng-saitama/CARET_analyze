# Copyright 2021 Research Institute of Systems Planning, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .callback_name import CallbackName
from .value_object import ValueObject


class Subscription(ValueObject):
    """Subscription info."""

    def __init__(
        self,
        node_name: str,
        topic_name: str,
        callback_name: str
    ) -> None:
        self._node_name: str = node_name
        self._topic_name: str = topic_name
        self._callback_name = CallbackName(node_name,  callback_name)

    @property
    def node_name(self) -> str:
        return self._node_name

    @property
    def topic_name(self) -> str:
        return self._topic_name

    @property
    def callback_name(self) -> str:
        return self._callback_name.name

    @property
    def callback_unique_name(self) -> str:
        return self._callback_name.unique_name
