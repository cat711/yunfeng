const user = document.getElementById("user");
const Pass = document.getElementById("pass");
const alt = document.getElementById("alt");
user.onclick = function () {
  var acn = document.getElementById("acn").value;
  var password = document.getElementById("PASS").value;

  console.log(acn);
  console.log(password);

  if (!acn) {
    alert("请输入账号");
    return 0;
  }
  if (!password) {
    alert("请输入密码");
    return 0;
  }

  axios({
    url: "",
    method: "POST",
    data: {
      password: `${password}`,
      id: `${acn}`,
    },
  }).then(function (ist) {
    console.log("登录报文", ist.data.data.id);
    if (ist.data.data.id == "1") {
      if (ist.data.data.pw == "1") {
        confirm("成功");
        window.location.href = "";
      } else {
        confirm("密码错误");
        //该函数为使用户的密码错误提示正常显示 即只在第一次显示，后面再点击也不再增加
        var alt = document.getElementById("alt"); //获取当前页面的alt存在情况

        if (alt) {
          //若有则删
          Pass.removeChild(Pass.children[Pass.children.length - 1]);
        }
        var div = document.createElement("div");
        Pass.appendChild(div);
        div.id = "alt";
        div.innerHTML = "密码错误！";

        var alt = document.getElementById("alt"); //获取当前页面的alt存在情况

        if (!alt) {
          //若无则增
          var div = document.createElement("div");
          Pass.appendChild(div);
          div.id = "alt";
          div.innerHTML = "密码错误！";
        }
      }
    } else {
      confirm("账号不存在");
    }
  });
};
