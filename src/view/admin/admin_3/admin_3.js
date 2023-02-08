const userList = document.getElementById("userList");


//这个变量决定打印内容


//打印排行榜
// for (let i = 0; i < 20; i++) {
//   var li = document.createElement("li");
//   userList.appendChild(li);
//   userList.children[userList.children.length - 1].innerHTML = '111';
// }
// for (let i = 0; i < 10; i++) {
//   var li = document.createElement("li");
//   userList.appendChild(li);
//   userList.children[userList.children.length - 1].innerHTML = `${testdata2}`;
// }

//获取今天时间并算出周一到周日的时间并转为2023-1-31格式
var now = new Date();
var nowTime = now.getTime();
var day = now.getDay();
var oneDayTime = 24 * 60 * 60 * 1000;
//显示周一
var s_dateTime = nowTime - (day - 1) * oneDayTime;
//显示周日
var e_dateTime = nowTime + (7 - day) * oneDayTime;
//初始化日期时间
var s_date = new Date(s_dateTime);
var e_date = new Date(e_dateTime);

function add0(m) {
  return m < 10 ? "0" + m : m;
}
function format(shijianchuo) {
  //shijianchuo是整数，否则要parseInt转换
  var time = new Date(shijianchuo);
  var y = time.getFullYear();
  var m = time.getMonth() + 1;
  var d = time.getDate();
  //var h = time.getHours();
  //var mm = time.getMinutes();
  //var s = time.getSeconds();
  return y + "-" + add0(m) + "-" + add0(d);
  //return y+''+add0(m)+''+add0(d)+''+add0(h)+':'+add0(mm)+':'+add0(s);
}
console.log(format(s_date));
console.log(format(e_date));

s_date = format(s_date);
e_date = format(e_date)
// axios({
//   url: "",
//   method: "POST",
//   data: {
//     s_date: `${s_date}`,
//     e_date: `${e_date}`,
//   },
// });

axios({
  url: "http://m7u12i6p.shenzhuo.vip:47038/rank/show/",
  method: "GET",
  params: {
    s_date: `${s_date}`,
    e_date: `${e_date}`,
  },
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
}).then(function (List) {
  
  
  for (var i = 0; i < List.data.data.length; i++) {
    console.log("报文", List.data.data[i]);
    var testdata2 = List.data.data[i].name;
    var testdata3 = "请假次数：" + List.data.data[i].count;
    var testdata =
      `${testdata2}` + "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" + `${testdata3}`;
    var li = document.createElement("li");
    userList.appendChild(li);
   
    userList.children[userList.children.length - 1].innerHTML =
     `${testdata}`
  }
});
