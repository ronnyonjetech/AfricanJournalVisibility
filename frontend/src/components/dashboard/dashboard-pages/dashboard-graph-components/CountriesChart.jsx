import React from "react";
import { Doughnut } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import 'chartjs-plugin-datalabels';
import ChartDataLabels from "chartjs-plugin-datalabels";

ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);

function getShadeOfBlue() {
  // Generates a shade of blue
  const baseColor = "#7DB8DA"; // Base color
  const shade = Math.floor(Math.random() * 114); // Adjust the value range to control the darkness of the shade
  const red = parseInt(baseColor.slice(1, 3), 16);
  const green = parseInt(baseColor.slice(3, 5), 16);
  const blue = parseInt(baseColor.slice(5, 7), 16);

  // Adjust the RGB values to generate a darker shade
  const darkerRed = Math.max(0, red - shade);
  const darkerGreen = Math.max(0, green - shade);
  const darkerBlue = Math.max(0, blue - shade);

  // Convert the darker RGB values to a hexadecimal string
  const darkerColor = `#${darkerRed.toString(16)}${darkerGreen.toString(16)}${darkerBlue.toString(16)}`;

  return darkerColor;
}


function CountriesChart({ data }) {
  // Extracting countries labels from the data
  const countryLabels = data.map((item) => item[9]);

  // Counting occurrences of each country
  const countryCounts = countryLabels.reduce((acc, country) => {
    acc[country] = (acc[country] || 0) + 1;
    return acc;
  }, {});

  // Extracting unique country names and their counts
  const uniqueCountries = Object.keys(countryCounts);
  const countryData = uniqueCountries.map((country) => {
    return {
      label: country,
      value: countryCounts[country],
      // color: getRandomColor(),
      color: getShadeOfBlue(),
      cutout: "60%",
    };
  });

  const options = {
    plugins: {
      responsive: true,
      datalabels: {
        formatter: function (value) {
          let val = Math.round(value);
          return new Intl.NumberFormat("tr-TR").format(val); //for number format
        },
        color: "white",
        font: {
          weight: 'bold',
          size:14,
          family: 'poppins',
        },
      }
      
    },
    cutout: countryData.map((item) => item.cutout),
  };

  const finalData = {
    labels: countryData.map((item) => item.label),
    datasets: [
      {
        data: countryData.map((item) => item.value),
        backgroundColor: countryData.map((item) => item.color),
        borderColor: countryData.map((item) => item.color),
        borderWidth: 1,
        dataVisibility: new Array(countryData.length).fill(true),
      },
    ],
  };

  return <Doughnut data={finalData} options={options} />;
}

function getRandomColor() {
  // Generates a random hex color
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
}

export default CountriesChart;
