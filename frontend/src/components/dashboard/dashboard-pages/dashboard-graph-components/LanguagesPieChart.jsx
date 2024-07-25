import React from "react";
import { Pie } from "react-chartjs-2";
import chroma from "chroma-js";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import 'chartjs-plugin-datalabels';
import ChartDataLabels from "chartjs-plugin-datalabels";

// Importing datalabels plugin for Chart.js v2

ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels);

const LanguagesPieChart = ({ data }) => {
  // Extracting languages from the data
  const languages = data.map((entry) => entry[8]);

  // Counting occurrences of each language
  const languageCounts = languages.reduce((counts, language) => {
    counts[language] = (counts[language] || 0) + 1;
    return counts;
  }, {});

  // Formatting data for chart
  const languageLabels = Object.keys(languageCounts);
  const languageData = Object.values(languageCounts);

  // Generating colors based on the provided color
  const baseColor = "#252973";
  const colors = chroma
    .scale([baseColor, chroma(baseColor).brighten(2)])
    .colors(languageLabels.length);

  // Calculate percentages
  const total = languageData.reduce((acc, val) => acc + val, 0);
  const percentages = languageData.map(
    (value) => ((value / total) * 100).toFixed(0) + "%"
  );

  // Chart options
  const chartOptions = {
    title: {
      display: true,
      text: "Languages Distribution",
      fontSize: 15,
    },
    responsive: true,
    plugins: {
      datalabels: {
        formatter: (value, ctx) => {
          return (
            languageLabels[ctx.dataIndex] + "\n" + percentages[ctx.dataIndex]
          );
        },
        color: "#fff",
      },
    },
    legend: {
      display: false,
      position: "right",
    },
  };

  // Formatting data for chart
  const pieChartData = {
    labels: languageLabels,
    datasets: [
      {
        data: languageData,
        backgroundColor: colors,
        hoverBackgroundColor: colors.map((color) => chroma(color).darken()),
        borderWidth: 0,
      },
    ],
  };

  // Rendering the pie chart with custom labels
  const pieChart = <Pie data={pieChartData} options={chartOptions} />;

  return <div style={{ width: "100%", height: "auto" }}>{pieChart}</div>;
};

export default LanguagesPieChart;