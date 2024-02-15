(function ($) {
  "use strict";
  var instagramData;
  $(function () {
    Chart.defaults.global.legend.labels.usePointStyle = true;

    if ($("#inline-datepicker").length) {
      $("#inline-datepicker").datepicker({
        enableOnReadonly: true,
        todayHighlight: true,
        templates: {
          leftArrow: '<i class="mdi mdi-chevron-left"></i>',
          rightArrow: '<i class="mdi mdi-chevron-right"></i>',
        },
      });
    }
    // flot chart bar script
    $(function () {
      fetch('/api/likes_count/')
		  .then(response => response.json())
		  .then(data => {
		    var likesCount = data.platform_likes.map((item, index) => [index, item.account__platform, item.likes_count]);
		    var platformLikes = data.platform_likes;
		    var instagramLikes = platformLikes.filter(item => item.account__platform === 'Instagram').slice(-6);
		    var instagramData = instagramLikes.map((item, index) => [index, item.likes_count]);

				function transformValue(value) {
	        if (value >= 0 && value <= 60) return 1;
	        else if (value <= 159) return 2;
	        else if (value <= 300) return 3;
	        else if (value <= 450) return 4;
	        else if (value <= 650) return 5;
	        else if (value <= 850) return 6;
	        else if (value <= 1050) return 7;
	        else if (value <= 1500) return 8;
	        else return 9;
        }

				var transformedData = instagramData.map(item => [item[0], transformValue(item[1])]);

	      var data = [
		      ["0", transformedData[0] ? transformedData[0][1] : 0],
	        ["1", transformedData[1] ? transformedData[1][1] : 0],
	        ["2", transformedData[2] ? transformedData[2][1] : 0],
	        ["3", transformedData[3] ? transformedData[3][1] : 0],
	        ["4", transformedData[4] ? transformedData[4][1] : 0],
	        ["5", transformedData[5] ? transformedData[5][1] : 0],
	      ];
	      if ($("#earningChart").length) {
	        $.plot("#earningChart", [data], {
	          series: {
	            bars: {
	              show: true,
	              barWidth: 0.5,
	              align: "center",
	              fillColor: "#3f50f6",
	            },
	            color: "#ffab2d",
	            lines: {
	              fill: true,
	            },
	          },
	          xaxis: {
	            mode: "categories",
	            tickLength: 0,
	            ticks: [],
	          },
	          yaxis: {
	            ticks: [],
	          },
	          grid: {
	            borderWidth: 0,
	            labelMargin: 10,
	            hoverable: true,
	            clickable: true,
	            mouseActiveRadius: 6,
	          },
	        });
        }
      })
    });
    $(function () {
      fetch('/api/likes_count/')
		  .then(response => response.json())
		  .then(data => {
		    var likesCount = data.platform_likes.map((item, index) => [index, item.account__platform, item.likes_count]);
		    var platformLikes = data.platform_likes;
		    var instagramLikes = platformLikes.filter(item => item.account__platform === 'Tiktok').slice(-6);
		    var instagramData = instagramLikes.map((item, index) => [index, item.likes_count]);

				function transformValue(value) {
	        if (value >= 0 && value <= 60) return 1;
	        else if (value <= 159) return 2;
	        else if (value <= 300) return 3;
	        else if (value <= 450) return 4;
	        else if (value <= 650) return 5;
	        else if (value <= 850) return 6;
	        else if (value <= 1050) return 7;
	        else if (value <= 1500) return 8;
	        else return 9;
        }

				var transformedData = instagramData.map(item => [item[0], transformValue(item[1])]);
	      var data = [
	        ["0", transformedData[0] ? transformedData[0][1] : 0],
	        ["1", transformedData[1] ? transformedData[1][1] : 0],
	        ["2", transformedData[2] ? transformedData[2][1] : 0],
	        ["3", transformedData[3] ? transformedData[3][1] : 0],
	        ["4", transformedData[4] ? transformedData[4][1] : 0],
	        ["5", transformedData[5] ? transformedData[5][1] : 0],
	      ];

	      if ($("#productChart").length) {
	        $.plot("#productChart", [data], {
	          series: {
	            bars: {
	              show: true,
	              barWidth: 0.5,
	              align: "center",
	              fillColor: "#3f50f6",
	            },
	            color: "#bcc1f3",
	            lines: {
	              fill: true,
	            },
	          },
	          xaxis: {
	            mode: "categories",
	            tickLength: 0,
	            ticks: [],
	          },
	          yaxis: {
	            ticks: [],
	          },
	          grid: {
	            borderWidth: 0,
	            labelMargin: 10,
	            hoverable: true,
	            clickable: true,
	            mouseActiveRadius: 6,
	          },
	        });
	      }
	    })
    });
    $(function () {
      fetch('/api/likes_count/')
		  .then(response => response.json())
		  .then(data => {
		    var likesCount = data.platform_likes.map((item, index) => [index, item.account__platform, item.likes_count]);
		    var platformLikes = data.platform_likes;
		    var instagramLikes = platformLikes.filter(item => item.account__platform === 'Facebook').slice(-6);
		    var instagramData = instagramLikes.map((item, index) => [index, item.likes_count]);

				function transformValue(value) {
	        if (value >= 0 && value <= 60) return 1;
	        else if (value <= 159) return 2;
	        else if (value <= 300) return 3;
	        else if (value <= 450) return 4;
	        else if (value <= 650) return 5;
	        else if (value <= 850) return 6;
	        else if (value <= 1050) return 7;
	        else if (value <= 1500) return 8;
	        else return 9;
        }

				var transformedData = instagramData.map(item => [item[0], transformValue(item[1])]);
	      var data = [
	        ["0", transformedData[0] ? transformedData[0][1] : 0],
	        ["1", transformedData[1] ? transformedData[1][1] : 0],
	        ["2", transformedData[2] ? transformedData[2][1] : 0],
	        ["3", transformedData[3] ? transformedData[3][1] : 0],
	        ["4", transformedData[4] ? transformedData[4][1] : 0],
	        ["5", transformedData[5] ? transformedData[5][1] : 0],
	      ];

	      if ($("#orderChart").length) {
	        $.plot("#orderChart", [data], {
	          series: {
	            bars: {
	              show: true,
	              barWidth: 0.5,
	              align: "center",
	              fillColor: "#3f50f6",
	            },
	            color: "#3f50f6",
	            lines: {
	              fill: true,
	            },
	          },
	          xaxis: {
	            mode: "categories",
	            tickLength: 0,
	            ticks: [],
	          },
	          yaxis: {
	            ticks: [],
	          },
	          grid: {
	            borderWidth: 0,
	            labelMargin: 10,
	            hoverable: true,
	            clickable: true,
	            mouseActiveRadius: 6,
	          },
	        });
	      }
	    })
    });
    var areaData1 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: ["#e2f8f8"],
          borderColor: ["#00cccd"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptions1 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaDataDark1 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: ["#00cccd33"],
          borderColor: ["#00cccd"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptionsDark1 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaData2 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [13, 2, 15, 3, 19, 12],
          backgroundColor: ["#e2f8f8"],
          borderColor: ["#00cccd"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptions2 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaDataDark2 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [13, 2, 15, 3, 19, 12],
          backgroundColor: ["#00cccd33"],
          borderColor: ["#00cccd"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptionsDark2 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaData3 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 9, 13, 5, 12, 3],
          backgroundColor: ["#ffed92"],
          borderColor: ["#ffab2d"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptions3 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaDataDark3 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 9, 13, 5, 12, 3],
          backgroundColor: ["#ffed924f"],
          borderColor: ["#ffab2d"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptionsDark3 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaData4 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [2, 19, 13, 5, 12, 10],
          backgroundColor: ["#ffed92"],
          borderColor: ["#ffab2d"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptions4 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaDataDark4 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [2, 19, 13, 5, 12, 10],
          backgroundColor: ["#ffed924f"],
          borderColor: ["#ffab2d"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptionsDark4 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaData5 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 15, 2, 12],
          backgroundColor: ["#e2f8f8"],
          borderColor: ["#00cccd"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptions5 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    var areaDataDark5 = {
      labels: ["", "", "", "", ""],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 15, 2, 12],
          backgroundColor: ["#00cccd33"],
          borderColor: ["#00cccd"],
          borderWidth: 1,
          pointRadius: 0,
          fill: true, // 3: no fill
        },
      ],
    };
    var areaOptionsDark5 = {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              display: false,
            },
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
        xAxes: [
          {
            gridLines: {
              drawBorder: false,
              display: false,
            },
          },
        ],
      },
      legend: {
        display: false,
      },
    };
    if ($("#areaChart1").length) {
      var areaChartCanvas = $("#areaChart1").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaData1,
        options: areaOptions1,
      });
    }
    if ($("#areaChart2").length) {
      var areaChartCanvas = $("#areaChart2").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaData2,
        options: areaOptions2,
      });
    }
    if ($("#areaChart3").length) {
      var areaChartCanvas = $("#areaChart3").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaData3,
        options: areaOptions3,
      });
    }
    if ($("#areaChart4").length) {
      var areaChartCanvas = $("#areaChart4").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaData4,
        options: areaOptions4,
      });
    }
    if ($("#areaChart5").length) {
      var areaChartCanvas = $("#areaChart5").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaData5,
        options: areaOptions5,
      });
    }
    if ($("#areaChartDark1").length) {
      var areaChartCanvas = $("#areaChartDark1").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaDataDark1,
        options: areaOptionsDark1,
      });
    }
    if ($("#areaChartDark2").length) {
      var areaChartCanvas = $("#areaChartDark2").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaDataDark2,
        options: areaOptionsDark2,
      });
    }
    if ($("#areaChartDark3").length) {
      var areaChartCanvas = $("#areaChartDark3").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaDataDark3,
        options: areaOptionsDark3,
      });
    }
    if ($("#areaChartDark4").length) {
      var areaChartCanvas = $("#areaChartDark4").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaDataDark4,
        options: areaOptionsDark4,
      });
    }
    if ($("#areaChartDark5").length) {
      var areaChartCanvas = $("#areaChartDark5").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: "line",
        data: areaDataDark5,
        options: areaOptionsDark5,
      });
    }
    if ($("#surveyBar").length) {
      Chart.elements.Rectangle.prototype.draw = function () {
        var ctx = this._chart.ctx;
        var vm = this._view;
        var left, right, top, bottom, signX, signY, borderSkipped, radius;
        var borderWidth = vm.borderWidth;
        // Set Radius Here
        // If radius is large enough to cause drawing errors a max radius is imposed
        var cornerRadius = 10;

        if (!vm.horizontal) {
          // bar
          left = vm.x - vm.width / 2;
          right = vm.x + vm.width / 2;
          top = vm.y;
          bottom = vm.base;
          signX = 1;
          signY = bottom > top ? 1 : -1;
          borderSkipped = vm.borderSkipped || "bottom";
        } else {
          // horizontal bar
          left = vm.base;
          right = vm.x;
          top = vm.y - vm.height / 2;
          bottom = vm.y + vm.height / 2;
          signX = right > left ? 1 : -1;
          signY = 1;
          borderSkipped = vm.borderSkipped || "left";
        }

        // Canvas doesn't allow us to stroke inside the width so we can
        // adjust the sizes to fit if we're setting a stroke on the line
        if (borderWidth) {
          // borderWidth shold be less than bar width and bar height.
          var barSize = Math.min(
            Math.abs(left - right),
            Math.abs(top - bottom)
          );
          borderWidth = borderWidth > barSize ? barSize : borderWidth;
          var halfStroke = borderWidth / 2;
          // Adjust borderWidth when bar top position is near vm.base(zero).
          var borderLeft =
            left + (borderSkipped !== "left" ? halfStroke * signX : 0);
          var borderRight =
            right + (borderSkipped !== "right" ? -halfStroke * signX : 0);
          var borderTop =
            top + (borderSkipped !== "top" ? halfStroke * signY : 0);
          var borderBottom =
            bottom + (borderSkipped !== "bottom" ? -halfStroke * signY : 0);
          // not become a vertical line?
          if (borderLeft !== borderRight) {
            top = borderTop;
            bottom = borderBottom;
          }
          // not become a horizontal line?
          if (borderTop !== borderBottom) {
            left = borderLeft;
            right = borderRight;
          }
        }

        ctx.beginPath();
        ctx.fillStyle = vm.backgroundColor;
        ctx.strokeStyle = vm.borderColor;
        ctx.lineWidth = borderWidth;

        // Corner points, from bottom-left to bottom-right clockwise
        // | 1 2 |
        // | 0 3 |
        var corners = [
          [left, bottom],
          [left, top],
          [right, top],
          [right, bottom],
        ];

        // Find first (starting) corner with fallback to 'bottom'
        var borders = ["bottom", "left", "top", "right"];
        var startCorner = borders.indexOf(borderSkipped, 0);
        if (startCorner === -1) {
          startCorner = 0;
        }

        function cornerAt(index) {
          return corners[(startCorner + index) % 4];
        }

        // Draw rectangle from 'startCorner'
        var corner = cornerAt(0);
        var width, height, x, y, nextCorner, nextCornerId;
        ctx.moveTo(corner[0], corner[1]);

        for (var i = 1; i < 4; i++) {
          corner = cornerAt(i);
          nextCornerId = i + 1;
          if (nextCornerId == 4) {
            nextCornerId = 0;
          }

          nextCorner = cornerAt(nextCornerId);

          width = corners[2][0] - corners[1][0];
          height = corners[0][1] - corners[1][1];
          x = corners[1][0];
          y = corners[1][1];

          var radius = cornerRadius;

          // Fix radius being too large
          if (radius > height / 2) {
            radius = height / 2;
          }
          if (radius > width / 2) {
            radius = width / 2;
          }

          ctx.moveTo(x + radius, y);
          ctx.lineTo(x + width - radius, y);
          ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
          ctx.lineTo(x + width, y + height - radius);
          ctx.quadraticCurveTo(
            x + width,
            y + height,
            x + width - radius,
            y + height
          );
          ctx.lineTo(x + radius, y + height);
          ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
          ctx.lineTo(x, y + radius);
          ctx.quadraticCurveTo(x, y, x + radius, y);
        }

        ctx.fill();
        if (borderWidth) {
          ctx.stroke();
        }
      };
      var data = {
        labels: ["S", "M", "T", "W", "T", "F", "S"],
        datasets: [
          {
            data: [14, 12, 9, 15, 10, 12, 10],
            backgroundColor: "#3f50f6",
            borderColor: "#3f50f6",
            pointRadius: 0,
            lineTension: 0,
            borderWidth: 1,
          },
          {
            data: [17, 17, 17, 17, 17, 17, 17],
            backgroundColor: "#e6e6e6",
            borderColor: "#e6e6e6",
            pointRadius: 0,
            lineTension: 0,
            borderWidth: 1,
          },
        ],
      };
      var options = {
        responsive: true,
        legend: {
          display: false,
        },
        barRoundness: 1,
        scales: {
          xAxes: [
            {
              display: true,
              stacked: true,
              gridLines: {
                display: false,
                drawBorder: false,
              },
              barPercentage: 0.3,
            },
          ],
          yAxes: [
            {
              ticks: {
                display: false,
                beginAtZero: true,
              },
              display: true,
              gridLines: {
                display: false,
                drawBorder: false,
              },
            },
          ],
        },
      };
      var ctxBar = document.getElementById("surveyBar");
      var myBarChart = new Chart(ctxBar, {
        type: "bar",
        data: data,
        options: options,
      });
    }
    if ($("#surveyBarDark").length) {
      Chart.elements.Rectangle.prototype.draw = function () {
        var ctx = this._chart.ctx;
        var vm = this._view;
        var left, right, top, bottom, signX, signY, borderSkipped, radius;
        var borderWidth = vm.borderWidth;
        // Set Radius Here
        // If radius is large enough to cause drawing errors a max radius is imposed
        var cornerRadius = 10;

        if (!vm.horizontal) {
          // bar
          left = vm.x - vm.width / 2;
          right = vm.x + vm.width / 2;
          top = vm.y;
          bottom = vm.base;
          signX = 1;
          signY = bottom > top ? 1 : -1;
          borderSkipped = vm.borderSkipped || "bottom";
        } else {
          // horizontal bar
          left = vm.base;
          right = vm.x;
          top = vm.y - vm.height / 2;
          bottom = vm.y + vm.height / 2;
          signX = right > left ? 1 : -1;
          signY = 1;
          borderSkipped = vm.borderSkipped || "left";
        }

        // Canvas doesn't allow us to stroke inside the width so we can
        // adjust the sizes to fit if we're setting a stroke on the line
        if (borderWidth) {
          // borderWidth shold be less than bar width and bar height.
          var barSize = Math.min(
            Math.abs(left - right),
            Math.abs(top - bottom)
          );
          borderWidth = borderWidth > barSize ? barSize : borderWidth;
          var halfStroke = borderWidth / 2;
          // Adjust borderWidth when bar top position is near vm.base(zero).
          var borderLeft =
            left + (borderSkipped !== "left" ? halfStroke * signX : 0);
          var borderRight =
            right + (borderSkipped !== "right" ? -halfStroke * signX : 0);
          var borderTop =
            top + (borderSkipped !== "top" ? halfStroke * signY : 0);
          var borderBottom =
            bottom + (borderSkipped !== "bottom" ? -halfStroke * signY : 0);
          // not become a vertical line?
          if (borderLeft !== borderRight) {
            top = borderTop;
            bottom = borderBottom;
          }
          // not become a horizontal line?
          if (borderTop !== borderBottom) {
            left = borderLeft;
            right = borderRight;
          }
        }

        ctx.beginPath();
        ctx.fillStyle = vm.backgroundColor;
        ctx.strokeStyle = vm.borderColor;
        ctx.lineWidth = borderWidth;

        // Corner points, from bottom-left to bottom-right clockwise
        // | 1 2 |
        // | 0 3 |
        var corners = [
          [left, bottom],
          [left, top],
          [right, top],
          [right, bottom],
        ];

        // Find first (starting) corner with fallback to 'bottom'
        var borders = ["bottom", "left", "top", "right"];
        var startCorner = borders.indexOf(borderSkipped, 0);
        if (startCorner === -1) {
          startCorner = 0;
        }

        function cornerAt(index) {
          return corners[(startCorner + index) % 4];
        }

        // Draw rectangle from 'startCorner'
        var corner = cornerAt(0);
        var width, height, x, y, nextCorner, nextCornerId;
        ctx.moveTo(corner[0], corner[1]);

        for (var i = 1; i < 4; i++) {
          corner = cornerAt(i);
          nextCornerId = i + 1;
          if (nextCornerId == 4) {
            nextCornerId = 0;
          }

          nextCorner = cornerAt(nextCornerId);

          width = corners[2][0] - corners[1][0];
          height = corners[0][1] - corners[1][1];
          x = corners[1][0];
          y = corners[1][1];

          var radius = cornerRadius;

          // Fix radius being too large
          if (radius > height / 2) {
            radius = height / 2;
          }
          if (radius > width / 2) {
            radius = width / 2;
          }

          ctx.moveTo(x + radius, y);
          ctx.lineTo(x + width - radius, y);
          ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
          ctx.lineTo(x + width, y + height - radius);
          ctx.quadraticCurveTo(
            x + width,
            y + height,
            x + width - radius,
            y + height
          );
          ctx.lineTo(x + radius, y + height);
          ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
          ctx.lineTo(x, y + radius);
          ctx.quadraticCurveTo(x, y, x + radius, y);
        }

        ctx.fill();
        if (borderWidth) {
          ctx.stroke();
        }
      };
      var data = {
        labels: ["S", "M", "T", "W", "T", "F", "S"],
        datasets: [
          {
            data: [14, 12, 9, 15, 10, 12, 10],
            backgroundColor: "#3f50f6",
            borderColor: "#3f50f6",
            pointRadius: 0,
            lineTension: 0,
            borderWidth: 1,
          },
          {
            data: [17, 17, 17, 17, 17, 17, 17],
            backgroundColor: "#383e5d",
            borderColor: "#383e5d",
            pointRadius: 0,
            lineTension: 0,
            borderWidth: 1,
          },
        ],
      };
      var options = {
        responsive: true,
        legend: {
          display: false,
        },
        barRoundness: 1,
        scales: {
          xAxes: [
            {
              display: true,
              stacked: true,
              gridLines: {
                display: false,
                drawBorder: false,
              },
              barPercentage: 0.3,
            },
          ],
          yAxes: [
            {
              ticks: {
                display: false,
                beginAtZero: true,
              },
              display: true,
              gridLines: {
                display: false,
                drawBorder: false,
              },
            },
          ],
        },
      };
      var ctxBar = document.getElementById("surveyBarDark");
      var myBarChart = new Chart(ctxBar, {
        type: "bar",
        data: data,
        options: options,
      });
    }

    // flot chart script
    $(function () {
      "use strict";
			fetch('/api/likes_count/')
		  .then(response => response.json())
		  .then(data => {
		    var likesCount = data.platform_likes.map((item, index) => [index, item.account__platform, item.likes_count]);
		    var platformLikes = data.platform_likes;
		    var facebookLikes = platformLikes.filter(item => item.account__platform === 'Facebook').slice(-80);
		    var facebookData = facebookLikes.map((item, index) => [index, item.likes_count]);
		    var tiktokLikes = platformLikes.filter(item => item.account__platform === 'Tiktok').slice(-80);
		    var tiktokData = tiktokLikes.map((item, index) => [index, item.likes_count]);
		    var instagramLikes = platformLikes.filter(item => item.account__platform === 'Instagram').slice(-80);
		    var instagramData = instagramLikes.map((item, index) => [index, item.likes_count]);

				function transformValue(value) {
	        if (value >= 0 && value <= 60) return 1;
	        else if (value <= 159) return 2;
	        else if (value <= 300) return 3;
	        else if (value <= 450) return 4;
	        else if (value <= 650) return 5;
	        else if (value <= 850) return 6;
	        else if (value <= 1050) return 7;
	        else if (value <= 1500) return 8;
	        else return 9;
        }

				var transFacebookData = facebookData.map(item => [item[0], transformValue(item[1])]);
				var transTiktokData = tiktokData.map(item => [item[0], transformValue(item[1])]);
				var transInstagramData = instagramData.map(item => [item[0], transformValue(item[1])]);
				// INSTAGRAM
	      var dashData2 = [];

	      for (var i = 0; i < 79; i++) {
			    var value = transInstagramData[i] ? transInstagramData[i][1] : 0;
			    dashData2.push([i, value]);
				}

				// FACEBOOK
	      var dashData3 = [];

	      for (var i = 0; i < 79; i++) {
			    var value = transFacebookData[i] ? transFacebookData[i][1] : 0;
			    dashData3.push([i, value]);
				}

				// TIKTOK
	      var dashData4 = [];

	      for (var i = 0; i < 79; i++) {
			    var value = transTiktokData[i] ? transTiktokData[i][1] : 0;
			    dashData4.push([i, value]);
				}

	      function bgFlotData(num, val) {
	        var data = [];
	        for (var i = 0; i < num; ++i) {
	          data.push([i, val]);
	        }
	        return data;
	      }

	      function bgFlotData(num, val) {
	        var data = [];
	        for (var i = 0; i < num; ++i) {
	          data.push([i, val]);
	        }
	        return data;
	      }

	      var plot = $.plot(
	        "#flotChart",
	        [
	          {
	            data: dashData4,
	            color: "#bcc1f3",
	            lines: {
	              fillColor: "#bcc1f3",
	            },
	          },
	          {
	            data: dashData3,
	            color: "#3f50f6",
	            lines: {
	              fillColor: "#3f50f6",
	            },
	          },
	          {
	            data: dashData2,
	            color: "#ffab2d",
	            lines: {
	              fillColor: { colors: [{ opacity: 0 }, { opacity: 0 }] },
	            },
	          },
	        ],
	        {
	          series: {
	            shadowSize: 0,
	            lines: {
	              show: true,
	              lineWidth: 2,
	              fill: true,
	            },
	          },
	          grid: {
	            borderWidth: 0,
	            labelMargin: 9,
	          },
	          yaxis: {
	            show: true,
	            min: 0,
	            max: 100,
	            ticks: true,
	          },
	          xaxis: {
	            show: true,
	            color: "#fff",
	            tickColor: "#eee",
	            ticks: [
	              [0, "0-9"],
	              [10, "10-19"],
	              [20, "20-29"],
	              [30, "30-39"],
	              [40, "40-49"],
	              [50, "50-59"],
	              [60, "60-69"],
	              [70, "70-79"],
	            ],
	          },
	        }
	      );
	    })
    });
  });
})(jQuery);
