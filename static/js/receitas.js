/* array com o id de cada card de receita */

const array_receitas = [
    { id: "r1", like: 13, dislike: 6 },
    { id: "r2", like: 6, dislike: 3 },
    { id: "r3", like: 12, dislike: 8 },
    { id: "r4", like: 8, dislike: 1 },
    { id: "r5", like: 5, dislike: 7 },
    { id: "r6", like: 7, dislike: 3 }
]

/* para cada elemento de card */

for (let obj of array_receitas) { // é preciso definir obj como let, se não os listeners não vão funcionar

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
