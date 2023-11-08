const navBar = $(".mobile");
const menuBtn = $(".hamburger-menu");
const app = $(".app");

const html = $("html");
const body = $("body");

app.click(function() {
    navBar.removeClass("nav-active");
    menuBtn.removeClass("toggle");
    html.removeClass("scroll-disable");
    body.removeClass("scroll-disable");
    $(".app").css("filter","none");
});

$(document).ready(function(){
    menuBtn.click(function() {
        navBar.toggleClass("nav-active");
        menuBtn.toggleClass("toggle");
        html.toggleClass("scroll-disable");
        body.toggleClass("scroll-disable");
        if ($(".app").css("filter") == "none") {
            $(".app").css("filter","blur(2px)");
        }
        else {
            $(".app").css("filter","none");
        }
    });
});

const month = document.querySelector("span.month");

switch (month.textContent) {
    case "Farvardin":
        month.textContent = "فروردین"
        break;

    case "Ordibehesht":
        month.textContent = "اردیبهشت"
        break;

    case "Khordad":
        month.textContent = "خرداد"
        break;

    case "Tir":
        month.textContent = "تیر"
        break;

    case "Mordad":
        month.textContent = "مرداد"
        break;

    case "Shahrivar":
        month.textContent = "شهریور"
        break;

    case "Mehr":
        month.textContent = "مهر"
        break;

    case "Aban":
        month.textContent = "آبان"
        break;

    case "Azar":
        month.textContent = "آذر"
        break;

    case "Dey":
        month.textContent = "دی"
        break;

    case "Bahman":
        month.textContent = "بهمن"
        break;

    case "Esfand":
        month.textContent = "اسفند"
        break;

    default:
        break;
}

const day = document.querySelector("span.day");

switch (day.textContent) {
    case "Satursday":
        day.textContent = "شنبه"
        break;

    case "Sunday":
        day.textContent = "یکشنبه"
        break;

    case "Monday":
        day.textContent = "دوشنبه"
        break;

    case "Tuesday":
        day.textContent = "سه شنبه"
        break;

    case "Wednesday":
        day.textContent = "چهارشنبه"
        break;

    case "Thursday":
        day.textContent = "پنجشنبه"
        break;

    case "Friday":
        day.textContent = "جمعه"
        break;

    default:
        break;
}