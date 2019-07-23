"use strict";

const el = React.createElement;

class Schedules extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stations: [
        { station: "radio1", schedule: [] },
        { station: "radio2", schedule: [] }
      ],
      message: "train"
    };

    this.getStation = this.getStation.bind(this);
    this.getButtonGroup = this.getButtonGroup.bind(this);
    this.handleDecrement = this.handleDecrement.bind(this);
    this.handleIncrement = this.handleIncrement.bind(this);
  }

  componentDidMount() {
    const { stations } = this.state;
    this.getStation("radio1")
      .then(response => response.json())
      .then(data => {
        const stationIndex = stations.findIndex(item => item.station === "radio1");
        stations[stationIndex].schedule = data.schedule;

        this.setState({ stations });
      });

    this.getStation("radio2")
      .then(response => response.json())
      .then(data => {
        const stationIndex = stations.findIndex(item => item.station === "radio2");
        stations[stationIndex].schedule = data.schedule;

        this.setState({ stations });
      });
  }

  componentDidUpdate(prevProps, prevState) {
    const { stations } = this.state;

    if (stations !== prevState.stations) {
    }
  }

  getStation(name) {
    switch (name) {
      case "radio1":
        return fetch(
          "https://scout.now.sh/api/cbc/schedules?station=cbc_radio_one"
        );
      case "radio2":
        return fetch(
          "https://scout.now.sh/api/cbc/schedules?station=cbc_radio_two"
        );
      default:
        return fetch(
          "https://scout.now.sh/api/cbc/schedules?station=cbc_radio_one"
        );
    }
  }

  handleIncrement() {}

  handleDecrement() {}

  getButtonGroup() {
    const { message, stations } = this.state;

    console.log(stations)

    const radio1 = stations.find( item => item.station === "radio1");

    const radio1List = radio1.schedule.map((listValue, idx) => {
        return React.createElement("li", {key: idx}, listValue.title);
      })


    return el(
      "div",
      null,
      el("ul", null, radio1List),
      el("button", { onClick: this.handleIncrement }, "Increment"),
      el("button", { onClick: this.handleDecrement }, "Decrement"),
      el("p", null, message)
    );
  }

  render() {
    if (this.state.liked) {
      return "You liked this.";
    }

    return this.getButtonGroup();
  }
}

const domContainer = document.querySelector("#schedules");
ReactDOM.render(el(Schedules), domContainer);
