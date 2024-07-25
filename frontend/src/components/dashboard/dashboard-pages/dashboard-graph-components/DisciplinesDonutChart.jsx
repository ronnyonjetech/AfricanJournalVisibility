import React, { useEffect, useRef } from "react";
import Chart from "chart.js/auto";
import ChartDataLabels from "chartjs-plugin-datalabels";

const DisciplinesDonutChart = ({ data }) => {
  const chartContainer = useRef(null);
  const chartInstance = useRef(null);

  useEffect(() => {
    if (chartInstance.current !== null) {
      chartInstance.current.destroy();
    }

    if (chartContainer && chartContainer.current) {
      const categories = data.map((entry) => entry[3]); // Extract categories from data
      const counts = {};
      categories.forEach((category) => {
        counts[category] = (counts[category] || 0) + 1;
      });

      const backgroundColors = generateShades(
        "#7DB8DA",
        Object.keys(counts).length
      );

      const ctx = chartContainer.current.getContext("2d");
      chartInstance.current = new Chart(ctx, {
        type: "polarArea",
        data: {
          labels: Object.keys(counts),
          datasets: [
            {
              label: "Discipline",
              data: Object.values(counts),
              backgroundColor: backgroundColors,
              borderColor: "#ffffff", // Border color
              borderWidth: 0,
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: true, // Hide default legend
              position: "right",
            },
            tooltips: {
              callbacks: {
                label: function (context) {
                  const label = context.label || "";
                  const value = context.formattedValue || "";
                  return `${label}: ${value}`;
                },
              },
            },
            title: {
              display: false,
              text: "Discipline Distribution",
            },
            labels: {
              render: "label",
              fontColor: "#000",
              precision: 0,
              fontSize: 14,
              fontStyle: "bold",
              arc: true,
            },
          },
        },
      });
    }

    // Cleanup function
    return () => {
      if (chartInstance.current !== null) {
        chartInstance.current.destroy();
      }
    };
  }, [data]);

  // Function to generate shades of a color
  const generateShades = (color, numShades) => {
    const shades = [];
    for (let i = 0; i < numShades; i++) {
      const shade = lightenDarkenColor(color, i * -10);
      shades.push(shade);
    }
    return shades;
  };

  // Function to lighten or darken a color
  const lightenDarkenColor = (col, amt) => {
    let usePound = false;
    if (col[0] === "#") {
      col = col.slice(1);
      usePound = true;
    }
    let num = parseInt(col, 16);
    let r = (num >> 16) + amt;
    if (r > 255) r = 255;
    else if (r < 0) r = 0;
    let b = ((num >> 8) & 0x00ff) + amt;
    if (b > 255) b = 255;
    else if (b < 0) b = 0;
    let g = (num & 0x0000ff) + amt;
    if (g > 255) g = 255;
    else if (g < 0) g = 0;
    return (
      (usePound ? "#" : "") +
      (g | (b << 8) | (r << 16)).toString(16).padStart(6, "0")
    );
  };

  return <canvas ref={chartContainer} />;
};

export default DisciplinesDonutChart;
