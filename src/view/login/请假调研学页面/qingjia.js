//得到当前日期
var time0 = document.querySelector('.time');
var date = new Date();
var year = date.getFullYear();
var month = date.getMonth() + 1;
var dates = date.getDate();
year = year < 10 ? '0' + year : year;
month = month < 10 ? '0' + month : month;
dates = dates < 10 ? '0' + dates : dates;
time0.innerHTML = year + '-' + month + '-' + dates;

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
    //var h = time.getHours();
    //var mm = time.getMinutes();
    //var s = time.getSeconds();
    return y + '-' + add0(m) + '-' + add0(d);
}
// console.log(format(monday));
// console.log(format(sunday));
var first = format(monday);
var two = format(sunday);
// console.log(first);
// console.log(two);

//切换日历框的样式
var defaultDate = document.querySelectorAll('.date-picker');
for (var i = 0; i < defaultDate.length; i++) {
    defaultDate[i].valueAsDate = new Date();
}

// axios.default.baseURL = 'http://m7u12i6p.shenzhuo.vip:47038/';
axios({
    url: 'http://m7u12i6p.shenzhuo.vip:47038/leave/show/',
    method: 'GET',
    contentType: "application/json",
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    params: {
        s_date: `${first}`,
        e_date: `${two}`,
    }
}).then(function (data) {
    // console.log(data.data);
    x = data.data.counts;
    // console.log(x);
    var obj = data.data.data;
    // console.log(obj);
    // console.log(data.counts);
    // })
    for (var j = 0; j < obj.length; j++) {
        // one += data[j];
        // console.log(obj[0]);
        var ini_day = obj[j].ini_day;
        var day = obj[j].day;
        var number = obj[j].time;
        var reason = obj[j].reason;
        // var indexs = selects.selectedIndex;
        // var num = selects.options[indexs].innerHTML;
        var div = document.createElement('div');
        jilu.insertBefore(div, jilu.children[0]);
        div.className = 'jiatiao';
        div.innerHTML = '<p class="p1">请假时间：' + day + '</p><p class="p2">节数：' + number + '</p><p calss="p3">请假理由：' + reason + '</p><div class="p4">' + ini_day + '</div>';

    }
})

//为转换页面按钮添加绑定事件
var qingjia = document.querySelector(".qingjia");
var tiaozheng = document.querySelector('.tiaozheng');
var click = document.querySelector('.click');
qingjia.onclick = function () {
    this.style.borderBottom = '5px #649ad8 solid';
    tiaozheng.style.borderBottom = '';
}
tiaozheng.addEventListener('click', function () {
    this.style.borderBottom = '5px #649ad8 solid';
    qingjia.style.borderBottom = '';
})

//选中selecte框的选中值
var selects = document.getElementById("select");
onchange = function () {
    var indexs = selects.selectedIndex;  //选中项的索引
    // console.log(selects.options[indexs].value);
}

//添加假条
var tijiao = document.querySelector('.tijiao');
// var jiatiao = document.querySelector('.jiatiao');
var jilu = document.querySelector('.jilu');
var table6 = document.querySelector('.table6');
var textarea = document.querySelector('textarea');


var indexs = selects.selectedIndex;  //选中项的索引
var num = selects.options[indexs].innerHTML;

tijiao.onclick = function () {
    if (textarea.value == '') {
        alert('请先将假条填写完整!');
    }
    if (time0.innerHTML > table6.value) {
        alert('请假时间无效，请重新输入');
    }
    else {
        if (x >= 3 & table6.value != '' & textarea.value != '') {
            var popBox = document.getElementById("popBox");
            var content = document.querySelector('.content');
            var popLayer = document.getElementById("popLayer");
            popBox.style.display = "block";
            popLayer.style.display = "block";
            content.innerHTML = '提醒：本周请假次数已达' + x + '次，<br>是否继续提交！！<br>';
            var button1 = document.querySelector('.button1');
            var button2 = document.querySelector('.button2');
            /*点击关闭按钮*/
            // var close1 = false;
            var close1 = button1.onclick = function closeBox1() {

                //关闭提示窗口
                var popBox = document.getElementById("popBox");
                var popLayer = document.getElementById("popLayer");
                popBox.style.display = "none";
                popLayer.style.display = "none";
                return true;
            }
            button2.onclick = function closeBox2() {
                var popBox = document.getElementById("popBox");
                var popLayer = document.getElementById("popLayer");
                popBox.style.display = "none";
                popLayer.style.display = "none";
                return false;
            }
            if (close1) {
                var indexs = selects.selectedIndex;
                var num1 = selects.options[indexs].innerHTML;

                //向后端传递数据
                axios({
                    url: "http://m7u12i6p.shenzhuo.vip:47038/leave/create/",
                    method: "POST",
                    contentType: "application/json",
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    data: {
                        // id:`${1111}`,
                        ini_date: time0.innerHTML,
                        date: table6.value,
                        time: num1,
                        reason: textarea.value
                    }
                }).then(function (result) {
                    // console.log(result.data.result);
                    if (result.data.result == 1) {
                        // var indexs2 = selects.selectedIndex;
                        // var num = selects.options[indexs].innerHTML;
                        var div = document.createElement('div');
                        jilu.insertBefore(div, jilu.children[0]);
                        div.className = 'jiatiao';
                        div.innerHTML = '<p class="p1">请假时间：' + table6.value + '</p><p class="p2">节数：' + num + '</p><p calss="p3">请假理由：' + textarea.value + '</p><div class="p4">' + time0.innerHTML + '</div>';
                        x++;
                    }else if(result.data.result == 0) {
                        alert('今天已提交过一次，暂时无法提交！');
                    }
                })
            }

            var indexs = selects.selectedIndex;
            var num = selects.options[indexs].innerHTML;

        }
        else if (x < 3 & table6.value != '' & textarea.value != '') {
            axios({
                url: "http://m7u12i6p.shenzhuo.vip:47038/leave/create/",
                method: "POST",
                contentType: "application/json",
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                // heads: {
                //     "content-type": "application/x-www-form-urlencoded",
                // },
                data: {
                    //    id:,
                    ini_date: time0.innerHTML,
                    date: table6.value,
                    time: num,
                    reason: textarea.value
                }
            }).then(function (result) {
                // console.log(result.data.result);
                y = result.data.result;
                // })
                if (y == 1) {
                    var indexs = selects.selectedIndex;
                    var num = selects.options[indexs].innerHTML;
                    var div = document.createElement('div');
                    jilu.insertBefore(div, jilu.children[0]);
                    div.className = 'jiatiao';
                    div.innerHTML = '<p class="p1">请假时间：' + table6.value + '</p><p class="p2">节数：' + num + '</p><p calss="p3">请假理由：' + textarea.value + '</p><div class="p4">' + time.innerHTML + '</div>';
                    x++;
                }else if(y == 0) {
                    alert('今天已提交过一次，暂时无法提交！');
                }
            })
        }
    }

}
