//为页面切换按钮绑定事件
var qingjia = document.querySelector(".qingjia");
var tiaozheng = document.querySelector('.tiaozheng');
var click = document.querySelector('.click');
qingjia.onclick = function () {
    this.className = 'qingjia click';
}
tiaozheng.addEventListener('click', function () {
    this.className = 'tiaozheng click';
})

//获取当前日期
var time = document.querySelector('.time');
var date = new Date();
var year = date.getFullYear();
var month = date.getMonth() + 1;
var dates = date.getDate();
year = year < 10 ? '0' + year : year;
month = month < 10 ? '0' + month : month;
dates = dates < 10 ? '0' + dates : dates;
time.innerHTML = year + '-' + month + '-' + dates;

//返回本周星期一到星期日的具体日期
var nowTime = date.getTime();
var day = date.getDay();
var oneDayTime = 24 * 60 * 60 * 1000;
//显示周一
var MondayTime = nowTime - (day - 1) * oneDayTime;
//显示周日
var SundayTime = nowTime + (7 - day) * oneDayTime;
//初始化日期时间
var monday = new Date(MondayTime);
var sunday = new Date(SundayTime);
function add0(m) { return m < 10 ? '0' + m : m }
function format(shijianchuo) {
    //shijianchuo是整数，否则要parseInt转换
    var time = new Date(shijianchuo);
    var y = time.getFullYear();
    var m = time.getMonth() + 1;
    var d = time.getDate();
    return y + '-' + add0(m) + '-' + add0(d);
}
// console.log(format(monday));
// console.log(format(sunday));

//切换日历框的效果
var defaultDate = document.querySelectorAll('.date-picker');
for (var i = 0; i < defaultDate.length; i++) {
    defaultDate[i].valueAsDate = new Date();
}

//选择selecte框的选中值
var selects2 = document.getElementById("select2");
onchange = function () {
    var indexs2 = selects2.selectedIndex;  //选中项的索引
}
var selects3 = document.getElementById("select3");
onchange = function () {
    var indexs3 = selects3.selectedIndex;  //选中项的索引
}

// axios.default.baseURL = 'http://m7u12i6p.shenzhuo.vip:47038/';
axios({
    url: 'http://m7u12i6p.shenzhuo.vip:47038/adjust/show/',
    method: 'get',
    contentType: "application/json",
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    params: {
        // id: ,
        s_date: format(monday),
        e_date: format(sunday),
    }
}).then(function (data) {
    var obj = data.data.data;
    // var x = counts;
    // console.log(obj);
    // console.log(x);
    // })
    for (var j = 0; j < obj.length; j++) {
        // one += data[j];
        // console.log(obj[j]);
        var ini_day = obj[j].ini_day;
        var day1 = obj[j].be_day;
        var day2 = obj[j].day;
        var number1 = obj[j].be_adjust_time;
        var number2 = obj[j].adjust_time;
        var reason = obj[j].reason;
        // var indexs = selects.selectedIndex;
        // var num = selects.options[indexs].innerHTML;
        var div = document.createElement('div');
        jilu.insertBefore(div, jilu.children[0]);
        div.className = 'jiatiao';
        div.innerHTML = '<p class="p1">原时间：' + day1 + '   ' + '节数：' + number1 + '</p><p class="p2">调整后：' + day2 + '   ' + '节数：' + number2 + ' </p><p calss="p3">调整理由：' + reason + '</p><div class="p5">' + ini_day + '</div>';
    }
})

//添加假条
// var tijiao = document.querySelector('.tijiao');
var tijiao2 = document.querySelector('.tijiao2');
// var jiatiao = document.querySelector('.jiatiao');
var jilu = document.querySelector('.jilu');
var table4 = document.querySelector('.table4');
var table7 = document.querySelector('.table7');
var textarea = document.querySelector('textarea');

var indexs2 = selects2.selectedIndex;
var indexs3 = selects3.selectedIndex;
var num2 = selects2.options[indexs2].innerHTML;
var num3 = selects3.options[indexs3].innerHTML;

tijiao2.onclick = function () {
    if (textarea.value == '') {
        alert('请先将假条填写完整!');
    } else if (time.innerHTML > table4.value || table7.value < time.innerHTML) {
        alert('请假时间无效，请重新输入');
    } else {
        axios({
            url: "http://m7u12i6p.shenzhuo.vip:47038/adjust/create/",
            method: "POST",
            contentType: "application/json",
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            data: {
                //       id:,
                ini_date: time.innerHTML,
                be_date: table4.value,
                be_adjust_time: num2,
                date: table7.value,
                adjust_time: num3,
                reason: textarea.value
            }
        }).then(function (result) {
            // console.log(result.data.result);
            var y = result.data.result;
            // })
            if (y == 1) {
                var indexs2 = selects2.selectedIndex;
                var indexs3 = selects3.selectedIndex;
                var num2 = selects2.options[indexs2].innerHTML;
                var num3 = selects3.options[indexs3].innerHTML;
                var div = document.createElement('div');
                jilu.insertBefore(div, jilu.children[0]);
                div.className = 'jiatiao';
                div.innerHTML = '<p class="p1">原时间：' + table4.value + '   ' + '节数：' + num2 + '</p><p class="p2">调整后：' + table7.value + '   ' + '节数：' + num3 + ' </p><p calss="p3">调整理由：' + textarea.value + '</p><div class="p5">' + time.innerHTML + '</div>';
            }else if(y == 0) {
                alert('今天已提交过一次，暂时无法提交！');
            }
        })
    }
}
