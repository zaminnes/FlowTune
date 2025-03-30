export default class FlowtuneJS {
  constructor(data, { autoConfig = {} } = {}) {
    this.resources = data.resources;
    this.autoConfig = autoConfig;
  }

  run() {
    console.log("Running FlowtuneJS with:", this.autoConfig);
  }
}
