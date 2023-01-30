const time = document.getElementById("time");
const reg = document.getElementById("reg");
const list = document.getElementById("list");
const userlist = document.getElementById("userlist");

setInterval(function () {
  axios({
    baseURL: "https://api.reginvolver.cn/",
    url: "/common/time",
    method: "GET",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  }).then((response) => {
    time.innerText = `${response.data}`;
  });
}, 1000);

reg.onclick = function () {
  var acn = document.getElementById("acn").value;
  var password = document.getElementById("password").value;
  if (!acn) {
    alert("请输入账号");
    return 0;
  }
  if (!password) {
    alert("请输入密码");
    return 0;
  }
  axios({
    
    method: "POST",
    data: {
      password: `${password}`,
      username: `${acn}`,
    },
    heads: {
      "content-type": "application/x-www-form-urlencoded",
    },
  }).then(function (ist) {
    // JSON.stringify(ist.data);
    console.log("登录报文", ist.data.data.user_id);

    if (ist.data.data.user_id == "1") {
      if (ist.data.data.password == "1") {
        confirm("成功");
      } else {
        confirm("密码错误");
      }
    } else {
      confirm("账号不存在");
    }
  });
};
