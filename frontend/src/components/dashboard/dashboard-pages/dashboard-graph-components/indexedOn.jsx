import React, { useEffect, useRef } from "react";
import QuickChart from "quickchart-js"; // Using ES6 import syntax

function IndexedOn({ value, where="", color="#252973" }) {
  // Ensure value is passed as a prop
  const myChart = new QuickChart();
  myChart.setConfig({
    type: "doughnut",
    data: {
      datasets: [
        {
          data: [value, 100 - value],
          backgroundColor: [color, "#eee"],
          label: "Dataset 1",
          borderWidth: 0,
        },
      ],
      labels: ["A", "C"],
    },
    options: {
      circumference: Math.PI,
      rotation: Math.PI,
      cutoutPercentage: 75,
      layout: {
        padding: 40,
      },
      legend: {
        display: false,
      },
      plugins: {
        datalabels: {
          color: "#404040",
          anchor: "end",
          align: "end",
          formatter: (val) => (val === "" ? val + "%" : ""),
          // formatter:  val + "%",
          font: {
            size: 25,
            weight: "bold",
          },
        },
        doughnutlabel: {
          labels: [
            {
              text: value + "%",
              color: "#000",
              font: {
                size: 25,
                weight: "bold",
              },
            },
            {
              text: "\nIndexed on ",
              font: {
                size: 20,
              },
            },
            {
              text: "\n"+where,
              color: "#000",
              font: {
                size: 22,
                weight: "bold",
              },
            },
          ],
        },
      },
    },
  });
  return <img src={myChart.getUrl()} alt="Google Scholar" />;
}

export default IndexedOn;
