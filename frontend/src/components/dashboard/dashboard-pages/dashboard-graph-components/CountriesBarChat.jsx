import React from "react";
import { Bar } from "react-chartjs-2";

function CountriesChart({ data }) {
  // Extracting countries labels from the data
  const countryLabels = data.map((item) => item[9]);

  // Counting occurrences of each country
  const countryCounts = countryLabels.reduce((acc, country) => {
    acc[country] = (acc[country] || 0) + 1;
    return acc;
  }, {});

  // Extracting unique country names and their counts, sorting by count in descending order
  const uniqueCountries = Object.keys(countryCounts).sort(
    (a, b) => countryCounts[b] - countryCounts[a]
  );
  const maxCount = countryCounts[uniqueCountries[0]]; // Get the count of the most occurring country

  const countryData = uniqueCountries.map((country) => {
    const count = countryCounts[country];
    const opacity = count / maxCount; // Calculate opacity based on count
    const backgroundColor = `rgba(37, 41, 115, ${opacity})`; // Interpolate between base color and white
    return {
      label: country,
      value: count,
      backgroundColor: backgroundColor,
    };
  });

  const options = {
    indexAxis: "y",
    plugins: {
      legend: {
        display: false, // Hide legend
      },
      datalabels: {
        formatter: function (value) {
          let val = Math.round(value);
          return new Intl.NumberFormat("tr-TR").format(val); //for number format
        },
        color: "white",
        font: {
          weight: "normal",
          size: 11,
          family: "verdana",
        },
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: "Count", // Rename x-axis to "Count"
          color: "#9A9A9A",
          font: {
            // weight: "bold",
            size: 12,
            family: "verdana",
          },
        },
        ticks: {
          beginAtZero: true,
        },
      },
      y: {
        title: {
          display: true,
          text: "Country", // Rename y-axis to "Country"
          color: "#9A9A9A",
          font: {
            weight: "normal",
            size: 12,
            family: "verdana",
          },
        },
      },
    },
  };

  const finalData = {
    labels: countryData.map((item) => item.label),
    datasets: [
      {
        label: "Country Counts",
        data: countryData.map((item) => item.value),
        backgroundColor: countryData.map((item) => item.backgroundColor),
        borderWidth: 1,
      },
    ],
  };

  return <Bar data={finalData} options={options} />;
}

export default CountriesChart;
