<template>
  <div class="timeline-item" data-text="_">
    <div class="timeline__content">
      <router-link :to="{ name: 'MovieDetail', params: { id: movie.pk } }">
        <img class="timeline__img" :src="moviePosterPath" alt="" :id="movie.title">
      </router-link>
      <p class="timeline__content-title">{{ movie.release_date }}</p>
      <p class="timeline__content-desc">{{ movie.title }}</p>
    </div>
  </div>
</template>

<script
  src="https://code.jquery.com/jquery-3.6.0.js"
  integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
  crossorigin="anonymous"></script>

<script>
import MovieDetail from '@/components/MovieDetail'
import axios from 'axios'

export default {
  name: 'MovieListItem',
  components: {
    MovieDetail
  },
  data: function () {
    return {
      moviePosterPath: `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  },
  props: {
    movie: Object
  },
  
  mounted() {
    (function($) {
      $.fn.timeline = function() {
        var selectors = {
          id: $(this),
          item: $(this).find(".timeline-item"),
          activeClass: "timeline-item--active",
          img: ".timeline__img"
        };
        selectors.item.eq(0).addClass(selectors.activeClass);
        selectors.id.css(
          "background-image",
          "url(" +
            selectors.item
              .first()
              .find(selectors.img)
              .attr("src") +
            ")"
        );
        var itemLength = selectors.item.length;
        $(window).scroll(function() {
          var max, min;
          var pos = $(this).scrollTop();
          selectors.item.each(function(i) {
            min = $(this).offset().top;
            max = $(this).height() + $(this).offset().top;
            var that = $(this);
            if (i == itemLength - 2 && pos > min + $(this).height() / 2) {
              selectors.item.removeClass(selectors.activeClass);
              selectors.id.css(
                "background-image",
                "url(" +
                  selectors.item
                    .last()
                    .find(selectors.img)
                    .attr("src") +
                  ")"
              );
              selectors.item.last().addClass(selectors.activeClass);
            } else if (pos <= max - 45 && pos >= min) {
              selectors.id.css(
                "background-image",
                "url(" +
                  $(this)
                    .find(selectors.img)
                    .attr("src") +
                  ")"
              );
              selectors.item.removeClass(selectors.activeClass);
              $(this).addClass(selectors.activeClass);
            }
          });
        });
      };
    })(jQuery);

    $("#timeline-1").timeline();
  }
}
</script>

<style scoped>
  @import url("https://fonts.googleapis.com/css?family=Cardo|Pathway+Gothic+One");
.timeline {
  display: flex;
  margin: 0 auto;
  flex-wrap: wrap;
  flex-direction: column;
  max-width: 700px;
  position: relative;
}
.timeline__content-title {
  font-weight: normal;
  font-size: 66px;
  margin: -10px 0 0 0;
  transition: 0.4s;
  padding: 0 10px;
  box-sizing: border-box;
  font-family: "Pathway Gothic One", sans-serif;
  color: #fff;
}
.timeline__content-desc {
  margin: 0;
  font-size: 15px;
  box-sizing: border-box;
  color: rgba(255, 255, 255, 0.7);
  font-family: Cardo;
  font-weight: normal;
  font-family: "Pathway Gothic One", sans-serif;

  line-height: 25px;
}
.timeline:before {
  position: absolute;
  left: 50%;
  width: 2px;
  height: 100%;
  margin-left: -1px;
  content: "";
  background: rgba(255, 255, 255, 0.07);
}
@media only screen and (max-width: 767px) {
  .timeline:before {
    left: 40px;
  }
}
.timeline-item {
  padding: 40px 0;
  opacity: 0.3;
  filter: blur(2px);
  transition: 0.5s;
  box-sizing: border-box;
  width: calc(50% - 40px);
  display: flex;
  position: relative;
  transform: translateY(-80px);
}
.timeline-item:before {
  content: attr(data-text);
  letter-spacing: 3px;
  width: 100%;
  position: absolute;
  color: rgba(255, 255, 255, 0.5);
  font-size: 13px;
  font-family: "Pathway Gothic One", sans-serif;
  border-left: 2px solid rgba(255, 255, 255, 0.5);
  top: 70%;
  margin-top: -5px;
  padding-left: 15px;
  opacity: 0;
  right: calc(-100% - 56px);
}
.timeline-item:nth-child(even) {
  align-self: flex-end;
}
.timeline-item:nth-child(even):before {
  right: auto;
  text-align: right;
  left: calc(-100% - 56px);
  padding-left: 0;
  border-left: none;
  border-right: 2px solid rgba(255, 255, 255, 0.5);
  padding-right: 15px;
}
.timeline-item--active {
  opacity: 1;
  transform: translateY(0);
  filter: blur(0px);
}
.timeline-item--active:before {
  top: 50%;
  transition: 0.3s all 0.2s;
  opacity: 1;
}
.timeline-item--active .timeline__content-title {
  margin: -50px 0 20px 0;
}
@media only screen and (max-width: 767px) {
  .timeline-item {
    align-self: baseline !important;
    width: 100%;
    padding: 0 30px 150px 80px;
  }
  .timeline-item:before {
    left: 10px !important;
    padding: 0 !important;
    top: 50px;
    text-align: center !important;
    width: 60px;
    border: none !important;
  }
  .timeline-item:last-child {
    padding-bottom: 40px;
  }
}
.timeline__img {
  max-width: 100%;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.4);
}
.timeline-container {
  width: 100%;
  position: relative;
  padding: 80px 0;
  transition: 0.3s ease 0s;
  background-attachment: fixed;
  background-size: cover;
}
.timeline-container:before {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(99, 99, 99, 0.8);
  content: "";
}
.timeline-header {
  width: 100%;
  text-align: center;
  margin-bottom: 80px;
  position: relative;
}
.timeline-header__title {
  color: #fff;
  font-size: 46px;
  font-family: Cardo;
  font-weight: normal;
  margin: 0;
}
.timeline-header__subtitle {
  color: rgba(255, 255, 255, 0.5);
  font-family: "Pathway Gothic One", sans-serif;
  font-size: 16px;
  letter-spacing: 5px;
  margin: 10px 0 0 0;
  font-weight: normal;
}

.demo-footer {
  padding: 60px 0;
  text-align: center;
}
.demo-footer a {
  color: #999;
  display: inline-block;
  font-family: Cardo;
}
</style>
