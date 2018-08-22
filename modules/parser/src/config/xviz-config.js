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

import XvizPrimitiveSettingsV1 from '../parsers/xviz-primitives-v1';
import XvizPrimitiveSettingsV2 from '../parsers/xviz-primitives-v2';

const DEFAULT_XVIZ_CONFIG = {
  // Config
  version: 2,

  DEFAULT_METADATA: {},

  PRIMARY_POSE_STREAM: 'vehicle-pose',
  // TODO - support multiple?
  OBJECT_STREAM: 'objects',

  filterStream: streamName => true, // Use to filter out unwanted streams

  postProcessMetadata: metadata => metadata,
  preProcessPrimitive: primitive => primitive, // Applied before normalize primitive
  postProcessTimeslice: timeslice => timeslice, // Post process timeslice
  postProcessVehiclePose: vehiclePose => vehiclePose, // Process vehicle pose from datum

  // TODO - these are used at render time instead of parse time. Need API audit
  postProcessFrame: frame => frame, // Post process log frame, used in LogSlice.getCurrentFrame
  getTrackedObjectPosition: _ => null,
  observeObjects: () => {}
};

const DEFAULT_XVIZ_SETTINGS = {
  TIME_WINDOW: 0.4,
  hiTimeResolution: 1 / 10, // Update pose and lightweight geometry up to 60Hz
  loTimeResolution: 1 / 10, // Throttle expensive geometry updates to 10Hz
  pathDistanceThreshold: 0.1 // Filters out close vertices (work around for PathLayer issue)
};

let xvizConfig = null;
const xvizSettings = Object.assign({}, DEFAULT_XVIZ_SETTINGS);

// CONFIG contains the static configuration of XVIZ (streams, how to postprocess etc)
export function setXvizConfig(config) {
  xvizConfig = Object.assign({}, DEFAULT_XVIZ_CONFIG, config);

  xvizConfig.PRIMITIVE_SETTINGS =
    xvizConfig.version === 1 ? XvizPrimitiveSettingsV1 : XvizPrimitiveSettingsV2;
}

export function getXvizConfig(config) {
  if (!xvizConfig) {
    throw new Error('Need to set XVIZ config');
  }
  return xvizConfig;
}

// SETTINGS are dynamic settings that can be changed during runtime by apps
export function setXvizSettings(config) {
  // TODO/OSS - offer a way to subscribe to settings changes
  Object.assign(xvizSettings, config);
}

export function getXvizSettings(config) {
  return xvizSettings;
}