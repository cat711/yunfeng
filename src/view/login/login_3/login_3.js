const uesrList = document.getElementById("userList");
const frequencyList = document.getElementById("frequencyList");

var testdata = "测试名字:xxx &nbsp &nbsp &nbsp 测试次数:5次";
var testdata2 = "测试次数:5次";

//打印排行榜
for (let i = 0; i < 10; i++) {
  var li = document.createElement("li");
  var btn = document.createElement("button");
  uesrList.appendChild(li);
  uesrList.children[uesrList.children.length - 1].innerHTML = `${testdata}`;
}

//获取今天时间并算出周一到周日的时间并转为2023-1-31格式
var now = new Date();
var nowTime = now.getTime();
var day = now.getDay();
var oneDayTime = 24 * 60 * 60 * 1000;
//显示周一
var MondayTime = nowTime - (day - 1) * oneDayTime;
//显示周日
var SundayTime = nowTime + (7 - day) * oneDayTime;
//初始化日期时间
var monday = new Date(MondayTime);
var sunday = new Date(SundayTime);

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
console.log(format(monday));
console.log(format(sunday));
