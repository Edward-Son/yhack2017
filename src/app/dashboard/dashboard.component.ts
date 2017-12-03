import { Component, OnInit } from '@angular/core';
import * as Chartist from 'chartist';
import {HttpClientModule, HttpClient, HttpHandler} from "@angular/common/http";
import {HttpModule, Http} from "@angular/http";
import 'rxjs/add/operator/map';
import * as go from 'gojs';




@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
})
export class DashboardComponent implements OnInit {

    temp = [];
    temp2 = [];
    temp3 = [];
    people = {firstName: null, lastName: null};
    personPrediction = [];
    companyPrediction = [];
    dotPlotX=[];
    dotPlotY=[];
    resolution1 = [];
    resolution2 = [];
    resolution = [];
    suspect = '';
    data: any;
    data2: any;
    predict: any;

  constructor(private http: Http) { }

  startAnimationForLineChart(chart){
      let seq: any, delays: any, durations: any;
      seq = 0;
      delays = 80;
      durations = 500;

      chart.on('draw', function(data) {
        if(data.type === 'line' || data.type === 'area') {
          data.element.animate({
            d: {
              begin: 600,
              dur: 700,
              from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
              to: data.path.clone().stringify(),
              easing: Chartist.Svg.Easing.easeOutQuint
            }
          });
        } else if(data.type === 'point') {
              seq++;
              data.element.animate({
                opacity: {
                  begin: seq * delays,
                  dur: durations,
                  from: 0,
                  to: 1,
                  easing: 'ease'
                }
              });
          }
      });

      seq = 0;
  };
  startAnimationForPieChart(chart){
      let seq2: any, delays2: any, durations2: any;

      seq2 = 0;
      delays2 = 80;
      durations2 = 500;
      chart.on('draw', function(data) {
          if(data.type === 'slice') {
              // Get the total path length in order to use for dash array animation
              var pathLength = data.element._node.getTotalLength();

              // Set a dasharray that matches the path length as prerequisite to animate dashoffset
              data.element.attr({
                  'stroke-dasharray': pathLength + 'px ' + pathLength + 'px'
              });

              // Create animation definition while also assigning an ID to the animation for later sync usage
              var animationDefinition = {
                  'stroke-dashoffset': {
                      id: 'anim' + data.index,
                      dur: 1000,
                      from: -pathLength + 'px',
                      to:  '0px',
                      easing: Chartist.Svg.Easing.easeOutQuint,
                      // We need to use `fill: 'freeze'` otherwise our animation will fall back to initial (not visible)
                      fill: 'freeze'
                  }
              };


              // We need to set an initial value before the animation starts as we are not in guided mode which would do that for us
              data.element.attr({
                  'stroke-dashoffset': -pathLength + 'px'
              });

              // We can't use guided mode as the animations need to rely on setting begin manually
              // See http://gionkunz.github.io/chartist-js/api-documentation.html#chartistsvg-function-animate
              data.element.animate(animationDefinition, false);
          }
      });

      seq2 = 0;
  };

    startAnimationForBarChart(chart){
        let seq2: any, delays2: any, durations2: any;

        seq2 = 0;
        delays2 = 80;
        durations2 = 500;
        chart.on('draw', function(data) {
            if(data.type === 'bar') {
                // Get the total path length in order to use for dash array animation
                var pathLength = data.element._node.getTotalLength();

                // Set a dasharray that matches the path length as prerequisite to animate dashoffset
                data.element.attr({
                    'stroke-dasharray': pathLength + 'px ' + pathLength + 'px'
                });

                // Create animation definition while also assigning an ID to the animation for later sync usage
                var animationDefinition = {
                    'stroke-dashoffset': {
                        id: 'anim' + data.index,
                        dur: 1000,
                        from: -pathLength + 'px',
                        to:  '0px',
                        easing: Chartist.Svg.Easing.easeOutQuint,
                        // We need to use `fill: 'freeze'` otherwise our animation will fall back to initial (not visible)
                        fill: 'freeze'
                    }
                };


                // We need to set an initial value before the animation starts as we are not in guided mode which would do that for us
                data.element.attr({
                    'stroke-dashoffset': -pathLength + 'px'
                });

                // We can't use guided mode as the animations need to rely on setting begin manually
                // See http://gionkunz.github.io/chartist-js/api-documentation.html#chartistsvg-function-animate
                data.element.animate(animationDefinition, false);
            }
        });

        seq2 = 0;
    };
  ngOnInit() {
      /* ----------==========     Daily Sales Chart initialization For Documentation    ==========---------- */

      const dataDailySalesChart: any = {
          labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
          series: [
              [12, 17, 7, 17, 23, 18, 38]
          ]
      };

     const optionsDailySalesChart: any = {
          lineSmooth: Chartist.Interpolation.cardinal({
              tension: 0
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: { top: 0, right: 0, bottom: 0, left: 0},
      };

      //var dailySalesChart = new Chartist.Line('#dailySalesChart', dataDailySalesChart, optionsDailySalesChart);

      //this.startAnimationForLineChart(dailySalesChart);

      // Create a simple bar chart

      var dataOtherBusiness = {
          labels: ['Barred brokers', 'All brokers'],
          series: [[57.6,53.5]]
      }

      var optionsBus = {
          width: 500,
          height: 400,
          high: 60,
          low: 50
      };

      var otherBusiness = new Chartist.Bar('#otherBusiness',dataOtherBusiness,optionsBus);

      this.startAnimationForBarChart(otherBusiness);

      var dataExams = {
          labels: ['Barred brokers', 'All brokers'],
          series: [[1.57,1.72]]
      }

      var optionsExams = {
          width: 500,
          height: 400,
          high: 1.8,
          low: 1.5
      };

      var testsTaken = new Chartist.Bar('#testsTaken',dataExams, optionsExams);

      this.startAnimationForBarChart(testsTaken);

      var dataCompany = {
          labels: ['Barred brokers', 'All brokers'],
          series: [[19.8,17.8]]
      }

      var optionsCompany = {
          width: 500,
          height: 400,
          high: 20,
          low: 16
      };


      var badCompany = new Chartist.Bar('#badCompany',dataCompany, optionsCompany);

      this.startAnimationForBarChart(badCompany);

      var dataAvgCompany = {
          labels: ['Barred brokers', 'All brokers'],
          series: [[28.4,25.2]]
      }

      var optionsAvgCompany = {
          width: 500,
          height: 400,
          high: 30,
          low: 24
      };


      var badAvgChart = new Chartist.Bar('#badAvgCompany',dataAvgCompany, optionsAvgCompany);

      this.startAnimationForBarChart(badAvgChart);



      /* ----------==========     Completed Tasks Chart initialization    ==========---------- */

      const dataCompletedTasksChart: any = {
          labels: this.dotPlotX,
          series: [
              this.dotPlotY
          ]
      };

     const optionsCompletedTasksChart: any = {
          lineSmooth: Chartist.Interpolation.cardinal({
              tension: 0
          }),
          low: 0,
          high: 16, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: { top: 0, right: 0, bottom: 0, left: 0}
      }

      var completedTasksChart = new Chartist.Line('#completedTasksChart', dataCompletedTasksChart, optionsCompletedTasksChart);

      // start animation for the Completed Tasks Chart - Line Chart
      this.startAnimationForLineChart(completedTasksChart);



      /* ----------==========     Pie Chart initialization    ==========---------- */

      var dataPieChart = {
          labels: ['60%'],
          series: [60],



      };
      var optionsPieChart = {
          labelInterpolationFnc: function(value) {
              return value[0]
          },
          donut: true,
          donutWidth: 15,
          startAngle: 0,
          total: 100,
          //showLabel: true
      };
      var responsiveOptions: any[] = [
          ['screen and (min-width: 640px)', {
              chartPadding: 300,
              labelOffset: 0,
              labelPosition: 'inside',
              labelInterpolationFnc: function(value) {
                  return value;
              }
          }],
          ['screen and (min-width: 1024px)', {
              labelOffset: 0,
              labelPosition: 'inside',
              chartPadding: 10
          }]

      ];
      var PieSubscriptionChart = new Chartist.Pie('#PieSubscriptionChart', dataPieChart, optionsPieChart, responsiveOptions);

      //start animation for the Emails Subscription Chart
      this.startAnimationForPieChart(PieSubscriptionChart);

      /* ----------==========     Emails Subscription Chart initialization    ==========---------- */

      var dataEmailsSubscriptionChart = {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          series: [
              [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]

          ]
      };
      var optionsEmailsSubscriptionChart = {
          axisX: {
              showGrid: false
          },
          low: 0,
          high: 1000,
          chartPadding: { top: 0, right: 5, bottom: 0, left: 0}
      };
      var responsiveOptions: any[] = [
          ['screen and (max-width: 640px)', {
              seriesBarDistance: 5,
              axisX: {
                  labelInterpolationFnc: function (value) {
                      return value[0];
                  }
              }
          }]
      ];
      var emailsSubscriptionChart = new Chartist.Bar('#emailsSubscriptionChart', dataEmailsSubscriptionChart, optionsEmailsSubscriptionChart, responsiveOptions);

      //start animation for the Emails Subscription Chart
      this.startAnimationForBarChart(emailsSubscriptionChart);

      this.getBadPeople().then((data) => {
          console.log("what is in the data ", data);
              //for(let bad of data){
              this.temp.push(data);
          for(let i =0;i<10;i++){
             // this.people.push(this.temp[0][i]);
              this.people['firstName'] = this.temp[0][i]['FIELD1'];
              this.people['lastName'] = this.temp[0][i]['FIELD2'];
              this.temp2.push(this.people['firstName'] +" "+ this.people['lastName']);
          }

      });

      this.getGuilty().then((data) => {
          console.log("what is in the data ", data);
          //for(let bad of data){
          let temp = [];
          for(let i =0;i<21;i++){
              /*if(i%2==0){
                  this.dotPlotX.push(temp[0][i]);
              }else{
                  this.dotPlotY.push(temp[0][i]*100);
              }*/
              this.dotPlotX.push(data["x"][i]);
              this.dotPlotY.push(data["y"][i]*100);
          }

      });




        this.personPrediction[0] = 25;
      this.companyPrediction[0] = 46;

      /*var $ = go.GraphObject.make;
      var myDiagram =
          $(go.Diagram, "myDiagramDiv",
              {
                  initialContentAlignment: go.Spot.Center, // center Diagram contents
                  "undoManager.isEnabled": true, // enable Ctrl-Z to undo and Ctrl-Y to redo
                  layout: $(go.TreeLayout, // specify a Diagram.layout that arranges trees
                      { angle: 90, layerSpacing: 35 })
              });
      // define a Link template that routes orthogonally, with no arrowhead
      myDiagram.linkTemplate =
          $(go.Link,
              { routing: go.Link.Orthogonal, corner: 5 },
              $(go.Shape, { strokeWidth: 3, stroke: "#555" })); // the link shape



      var myModel = $(go.TreeModel);
      // define a simple Node template
      myDiagram.nodeTemplate =
          $(go.Node, "Horizontal",
              // the entire node will have a light-blue background
              $(go.Shape,
                  "RoundedRectangle",
                  // Pictures should normally have an explicit width and height.
                  // This picture has a red background, only visible when there is no source set
                  // or when the image is partially transparent.
                  // Picture.source is data bound to the "source" attribute of the model data
                  {width: 350 , height:50},
                  new go.Binding("fill", "color")),
              $(go.TextBlock,
                  "Default",  // the initial value for TextBlock.text
                  // some room around the text, a larger font, and a white stroke:
                  { margin: -300, stroke: "white", font: "bold 16px sans-serif" },
                  // TextBlock.text is data bound to the "name" attribute of the model data
                  new go.Binding("text", "name"))
          );
// in the model data, each node is represented by a JavaScript object:
      myModel.nodeDataArray =
          [
              { key: 1, name: " Organizations Location", color: "lightyellow", parent: 7},
              { key: 2, name: "Organization Name", color: "#49b3c7", parent: 7},
              { key: 3, name: "Organization Branch", color: "#e8473c", parent:7 },
              { key: 4, name: "Location where the individual works", color: "#59b15c", parent: 1 },
              { key: 5, name:  "Number of Exams Taken", color: "#f49631", parent: 7 },
              { key: 6, name: "Is involved in other businesses", color: "#9f43b4", parent: 3},
              { key: 7, name: "Individual"},
      ];
      myDiagram.model = myModel;*/

      this.data2 = {'barred': [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
          'name': ['MATTHEW BROZOVIC',
              'MARK HANSON',
              'STEVEN WILLIAMSON',
              'TIMOTHY ROE',
              'JOHN BUCKLEY',
              'CAROL HENRICK',
              'DANIEL HOLZRICHTER',
              'VIVIAN ALEXANDER',
              'BRENT ION',
              'RICHARD BACHAND']};

      console.log("what is in the data ", this.data2);

      //for(let bad of data){
      //for(let i =0;i<10;i++){
         // this.resolution.push({r1: this.data2["name"][i], r2: this.data2["barred"][i], show: false});
      // this.resolution = [{name: 'MATTHEW BROZOVIC', barred: 0, show: false}];

      //}

      this.setTable();


  }

  getBadPeople(){
      if (this.data) {
          return Promise.resolve(this.data);
      }


      return new Promise(resolve => {
          this.http.get('assets/cleaned_bad_people.json')
              .map(res => res.json())
              .subscribe(data => {
                  this.data = data;
                  resolve(this.data);
              });
      });



  }

  getGuilty(){
      if (this.data) {
          return Promise.resolve(this.data);
      }


      return new Promise(resolve => {
          this.http.get('assets/guilty.json')
              .map(res => res.json())
              .subscribe(data => {
                  this.data = data;
                  resolve(this.data);
              });
      });

  }

  setTable(){
      this.data2 = {'barred': [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
          'name': ['MATTHEW BROZOVIC',
              'MARK HANSON',
              'STEVEN WILLIAMSON',
              'TIMOTHY ROE',
              'JOHN BUCKLEY',
              'CAROL HENRICK',
              'DANIEL HOLZRICHTER',
              'VIVIAN ALEXANDER',
              'BRENT ION',
              'RICHARD BACHAND']};

          console.log("what is in the data ", this.data2);

          //for(let bad of data){
          for(let i =0;i<10;i++){
              this.resolution.push({r1: this.data2["name"][i], r2: this.data2["barred"][i], show: false});

          }


  }

 findSuspect(){
     console.log(this.suspect);
    for(let i = 0; i <10; i++){
        console.log(this.resolution[i].r1);
        if(this.resolution[i].r1 == this.suspect){
            this.resolution[i].show = true;
            this.predict = this.resolution[i].r2;
            break;
        }
    }
 }



}
