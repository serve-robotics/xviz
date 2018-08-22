// Copyright (c) 2019 Uber Technologies, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import {setXvizConfig} from '../config/xviz-config';
import {parseStreamDataMessage} from '../parsers/parse-stream-data-message';
import {preSerialize} from '../parsers/serialize';

export default config => self => {
  setXvizConfig(config);

  function onResult(message) {
    const transfers = [];
    const {channels} = message;

    if (channels) {
      for (const streamName in channels) {
        const {pointCloud} = channels[streamName];
        if (pointCloud) {
          transfers.push(
            pointCloud.ids.buffer,
            pointCloud.colors.buffer,
            pointCloud.positions.buffer
          );
        }
      }
    }

    message = preSerialize(message);
    self.postMessage(message, transfers);
  }

  function onError(error) {
    throw error;
  }

  self.onmessage = e => {
    parseStreamDataMessage(e.data, onResult, onError);
  };
};