(function(){
    const $selects = document.querySelectorAll(".form-select");
    $selects.forEach(el => {
        el.addEventListener("change", e =>{
            moveTaskTo(el.getAttribute("data-id"), el.value);
        })
    });

const moveTaskTo = (id, value) =>{
    baseURL=document.URL
    window.location.replace(baseURL+`moveTask/${id}/${value}`)
}
})();

/*
(function () {
  let temporizador = setTimeout(() => {
    const $selects = document.querySelectorAll(".form-select");
    $selects.forEach((el) => {
      el.addEventListener("change", (e) => {
        moveTaskTo(el.getAttribute("data-id"), el.value);
      });
    });
  }, 10);

  const moveTaskTo = (id, value) => {
    console.log("id: ", id);
    console.log("valor: ", value);
  };
})();
*/