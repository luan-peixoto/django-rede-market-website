/* array com o id de cada card de noticia */

const array_noticias = [
    { id: "n1", like: 5, dislike: 3 },
    { id: "n2", like: 10, dislike: 5 },
    { id: "n3", like: 7, dislike: 3 },
    { id: "n4", like: 2, dislike: 4 },
    { id: "n5", like: 15, dislike: 6 },
    { id: "n6", like: 9, dislike: 4 }
]

/* para cada elemento de card */

for (let obj of array_noticias) { // é preciso definir obj como let, se não os listeners não vão funcionar

    /* criar div com botões de like */

    let div = `<span id="like-${obj.id}" class="badge bg-primary" data-like="${obj.like}"></span><a class="ps-1 pe-1" id="like-btn-${obj.id}" data-clicked="false" type="button" style="color: #0d6efd"><i id="like-icon-${obj.id}" class="far fa-thumbs-up"></i></a><span id="dislike-${obj.id}" class="badge bg-primary"  data-dislike="${obj.dislike}"></span><a class="ps-1 pe-1" id="dislike-btn-${obj.id}" data-clicked="false" type="button" style="color: #0d6efd"><i id="dislike-icon-${obj.id}" class="far fa-thumbs-down"></i></a>`
    $(`#${obj.id}`).append(div);

    /* inserir texto */

    $(`#like-${obj.id}`).text($(`#like-${obj.id}`).data("like"))
    $(`#dislike-${obj.id}`).text($(`#dislike-${obj.id}`).data("dislike"))

    /* criar um listener */

    $(`#like-btn-${obj.id}`).click(function () {
        let click = $(`#like-btn-${obj.id}`).data("clicked");

        if (!click) {
            let click_dislike = $(`#dislike-btn-${obj.id}`).data("clicked");
            if (click_dislike) {
                let n = $(`#dislike-${obj.id}`).data("dislike") - 1;
                $(`#dislike-${obj.id}`).data("dislike", n);
                $(`#dislike-${obj.id}`).text(n);
                $(`#dislike-btn-${obj.id}`).data("clicked", false);
                $(`#dislike-icon-${obj.id}`).removeClass("fas");
            };

            let n = $(`#like-${obj.id}`).data("like") + 1;
            $(`#like-${obj.id}`).data("like", n);
            $(`#like-${obj.id}`).text(n);
            $(`#like-btn-${obj.id}`).data("clicked", true);

            $(`#like-icon-${obj.id}`).addClass("fas");

            return;
        }
        let n = $(`#like-${obj.id}`).data("like") - 1;
        $(`#like-${obj.id}`).data("like", n);
        $(`#like-${obj.id}`).text(n);
        $(`#like-btn-${obj.id}`).data("clicked", false);

        $(`#like-icon-${obj.id}`).removeClass("fas");


    });

    $(`#dislike-btn-${obj.id}`).click(function () {
        let click = $(`#dislike-btn-${obj.id}`).data("clicked");
        if (!click) {
            let click_like = $(`#like-btn-${obj.id}`).data("clicked");
            if (click_like) {
                let n = $(`#like-${obj.id}`).data("like") - 1;
                $(`#like-${obj.id}`).data("like", n);
                $(`#like-${obj.id}`).text(n);
                $(`#like-btn-${obj.id}`).data("clicked", false);

                $(`#like-icon-${obj.id}`).removeClass("fas");
            };

            let n = $(`#dislike-${obj.id}`).data("dislike") + 1;
            $(`#dislike-${obj.id}`).data("dislike", n);
            $(`#dislike-${obj.id}`).text(n);
            $(`#dislike-btn-${obj.id}`).data("clicked", true);


            $(`#dislike-icon-${obj.id}`).addClass("fas");

            return;
        }
        let n = $(`#dislike-${obj.id}`).data("dislike") - 1;
        $(`#dislike-${obj.id}`).data("dislike", n);
        $(`#dislike-${obj.id}`).text(n);
        $(`#dislike-btn-${obj.id}`).data("clicked", false);

        $(`#dislike-icon-${obj.id}`).removeClass("fas");
    });

};

/* também poderia ser feito assim:

$("#n1, #n2, #n3, #n4, #n5, #n6").each(function() {
    let obj = {id: this.id}; // criando um obj que tenha id, pois o this tambem muda a pos a execucao
    // do each

    $(`#like-btn-${obj.id}`).click(function () {
        let click = $(`#like-btn-${obj.id}`).data("clicked");

        if (!click) {
            let click_dislike = $(`#dislike-btn-${obj.id}`).data("clicked");
            if (click_dislike) {
                let n = $(`#dislike-${obj.id}`).data("dislike") - 1;
                $(`#dislike-${obj.id}`).data("dislike", n);
                $(`#dislike-${obj.id}`).text(n);
                $(`#dislike-btn-${obj.id}`).data("clicked", false);
                $(`#dislike-icon-${obj.id}`).removeClass("fas");
            };

            let n = $(`#like-${obj.id}`).data("like") + 1;
            $(`#like-${obj.id}`).data("like", n);
            $(`#like-${obj.id}`).text(n);
            $(`#like-btn-${obj.id}`).data("clicked", true);

            $(`#like-icon-${obj.id}`).addClass("fas");

            return;
        }
        let n = $(`#like-${obj.id}`).data("like") - 1;
        $(`#like-${obj.id}`).data("like", n);
        $(`#like-${obj.id}`).text(n);
        $(`#like-btn-${obj.id}`).data("clicked", false);

        $(`#like-icon-${obj.id}`).removeClass("fas");


    });

    $(`#dislike-btn-${obj.id}`).click(function () {
        let click = $(`#dislike-btn-${obj.id}`).data("clicked");
        if (!click) {
            let click_like = $(`#like-btn-${obj.id}`).data("clicked");
            if (click_like) {
                let n = $(`#like-${obj.id}`).data("like") - 1;
                $(`#like-${obj.id}`).data("like", n);
                $(`#like-${obj.id}`).text(n);
                $(`#like-btn-${obj.id}`).data("clicked", false);

                $(`#like-icon-${obj.id}`).removeClass("fas");
            };

            let n = $(`#dislike-${obj.id}`).data("dislike") + 1;
            $(`#dislike-${obj.id}`).data("dislike", n);
            $(`#dislike-${obj.id}`).text(n);
            $(`#dislike-btn-${obj.id}`).data("clicked", true);


            $(`#dislike-icon-${obj.id}`).addClass("fas");

            return;
        }
        let n = $(`#dislike-${obj.id}`).data("dislike") - 1;
        $(`#dislike-${obj.id}`).data("dislike", n);
        $(`#dislike-${obj.id}`).text(n);
        $(`#dislike-btn-${obj.id}`).data("clicked", false);

        $(`#dislike-icon-${obj.id}`).removeClass("fas");
    });
});

*/