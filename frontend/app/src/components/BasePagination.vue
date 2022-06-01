<template>
  <div class="row justify-content-center">
    <div class="col-auto">
      <nav aria-label="Page navigation">
        <ul class="pagination">
          <li class="page-item" :class="{'disabled': currentPageEdited == 1}">
            <a class="page-link" href="#title" v-on:click.prevent="setPage(1);">&lt;&lt;</a>
          </li>
          <li class="page-item" :class="{'disabled': currentPageEdited == 1}">
            <a
              class="page-link"
              href="#title"
              v-on:click.prevent="setPage(currentPageEdited -1);"
              :class="{'disable':currentPageEdited == 1}"
            >&lt;</a>
          </li>
          <li
            class="page-item"
            v-for="num in showPagesFix"
            :key="num"
            :class="{'active' : numFix(num) == currentPageEdited}"
          >
            <template v-if="numFix(num) == currentPageEdited">
              <span class="page-link">{{ numFix(num) }}</span>
            </template>
            <a
              class="page-link"
              href="#title"
              v-on:click.prevent="setPage(numFix(num))"
              v-else
            >{{ numFix(num) }}</a>
          </li>
          <li class="page-item" :class="{'disabled': currentPageEdited == totalPages}">
            <a class="page-link" href="#title" v-on:click.prevent="setPage(currentPageEdited + 1);">&gt;</a>
          </li>
          <li class="page-item" :class="{'disabled': currentPageEdited == totalPages}">
            <a class="page-link" href="#title" v-on:click.prevent="setPage(totalPages);">&gt;&gt;</a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>
 
<script>
import { computed, ref, watch } from "@vue/runtime-core";
export default {
  name: "BasePagination",
  props: {
    showPages: {
      default: 1,
      require: false,
      type: Number,
    }, //ページネーションを何件表示するか
    currentPage: {
      default: 1,
      require: false,
      type: Number,
    }, //現在のページ
    totalCount: {
      default: 1,
      require: false,
      type: Number,
    }, //総件数
    totalPages: {
      default: 1,
      require: false,
      type: Number,
    }, //総ページ数
    perPage: {
      default: 20,
      require: false,
      type: Number,
    }, //1ページあたりの表示件数
  },
  emits: ["currentPage"],
  setup(props, { emit }) {
    const currentPageEdited = ref(props.currentPage);

    //ページ番号を計算する
    const numFix = (num) => {
      const ajust = 1 + (props.showPages - 1) / 2;
      let result = num;
      //前ページがマイナスになる場合は1からはじめる
      if (currentPageEdited.value > props.showPages / 2) {
        result = num + currentPageEdited.value - ajust;
      }
      //後ページが最大ページを超える場合は最大ページを超えないようにする
      if (currentPageEdited.value + props.showPages / 2 > props.totalPages) {
        result = props.totalPages - props.showPages + num;
      } //総ページ数が表示ページ数に満たない場合、連番そのまま
      if (props.totalPages <= props.showPages) {
        result = num;
      }
      return result;
    };

    //総記事数が表示ページ数以下の場合に調整する
    const showPagesFix = computed(() => {
      if (props.totalPages < props.showPages) {
        return props.totalPages;
      } else {
        return props.showPages;
      }
    });

    //ページネーションを複数設置したときの対応
    watch(
      () => props.currentPage,
      (newValule) => {
        currentPageEdited.value = newValule;
      }
    );

    //何ページ目を表示するか
    const setPage = (page) => {
      //マイナスにならないようにする
      if (page <= 0) {
        currentPageEdited.value = 1;
      }
      //最大ページを超えないようにする
      else if (page > props.totalPages) {
        currentPageEdited.value = props.totalPages;
      } else {
        currentPageEdited.value = page;
      }
      //親コンポーネントに現在のページを送る
      emit("currentPage", currentPageEdited.value);
    };

    return { currentPageEdited, numFix, setPage, showPagesFix };
  },
};
</script>