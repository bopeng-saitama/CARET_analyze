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

from caret_analyze.value_objects.value_object import ValueObject


class SampleClassA(ValueObject):

    def __init__(self, i: int, s: str) -> None:
        self._i = i
        self._s = s

    @property
    def i(self):
        return self._i

    @property
    def s(self):
        return self._s


class SampleClassB(ValueObject):

    def __init__(self, i: int, s: str) -> None:
        self._i = i
        self._s = s

    @property
    def i(self):
        return self._i

    @property
    def s(self):
        return self._s


class TestValueObject:

    def test_eq(self):
        assert SampleClassA(1, '1') == SampleClassA(1, '1')
        assert SampleClassA(1, '1') != SampleClassA(1, '2')
        assert SampleClassA(1, '1') != SampleClassA(2, '1')
        assert SampleClassA(1, '1') != SampleClassB(1, '1')

    def test_hash(self):
        assert hash(SampleClassA(1, '1')) == hash(SampleClassA(1, '1'))
        assert hash(SampleClassA(1, '1')) != hash(SampleClassA(1, '2'))
        assert hash(SampleClassA(1, '1')) != hash(SampleClassA(2, '1'))
        assert hash(SampleClassA(1, '1')) != hash(SampleClassB(1, '1'))
