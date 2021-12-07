function like_click(id_noticia) {

    let click = $(`#like-btn-${id_noticia}`).data("clicked");

    if (!click) {
        let click_dislike = $(`#dislike-btn-${id_noticia}`).data("clicked");
        if (click_dislike) {
            let n = $(`#dislike-${id_noticia}`).data("dislike") - 1;
            $(`#dislike-${id_noticia}`).data("dislike", n);
            $(`#dislike-${id_noticia}`).text(n);
            $(`#dislike-btn-${id_noticia}`).data("clicked", false);
            $(`#dislike-icon-${id_noticia}`).removeClass("fas");
        };

        let n = $(`#like-${id_noticia}`).data("like") + 1;
        $(`#like-${id_noticia}`).data("like", n);
        $(`#like-${id_noticia}`).text(n);
        $(`#like-btn-${id_noticia}`).data("clicked", true);

        $(`#like-icon-${id_noticia}`).addClass("fas");

        return;
    }
    let n = $(`#like-${id_noticia}`).data("like") - 1;
    $(`#like-${id_noticia}`).data("like", n);
    $(`#like-${id_noticia}`).text(n);
    $(`#like-btn-${id_noticia}`).data("clicked", false);

    $(`#like-icon-${id_noticia}`).removeClass("fas");



}

function dislike_click(id_noticia) {

    let click = $(`#dislike-btn-${id_noticia}`).data("clicked");
    if (!click) {
        let click_like = $(`#like-btn-${id_noticia}`).data("clicked");
        if (click_like) {
            let n = $(`#like-${id_noticia}`).data("like") - 1;
            $(`#like-${id_noticia}`).data("like", n);
            $(`#like-${id_noticia}`).text(n);
            $(`#like-btn-${id_noticia}`).data("clicked", false);

            $(`#like-icon-${id_noticia}`).removeClass("fas");
        };

        let n = $(`#dislike-${id_noticia}`).data("dislike") + 1;
        $(`#dislike-${id_noticia}`).data("dislike", n);
        $(`#dislike-${id_noticia}`).text(n);
        $(`#dislike-btn-${id_noticia}`).data("clicked", true);


        $(`#dislike-icon-${id_noticia}`).addClass("fas");

        return;
    }
    let n = $(`#dislike-${id_noticia}`).data("dislike") - 1;
    $(`#dislike-${id_noticia}`).data("dislike", n);
    $(`#dislike-${id_noticia}`).text(n);
    $(`#dislike-btn-${id_noticia}`).data("clicked", false);

    $(`#dislike-icon-${id_noticia}`).removeClass("fas");

}