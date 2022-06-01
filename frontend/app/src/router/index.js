import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import NovelDetail from '../views/NovelDetail.vue'
import SimilarNovelDatas from '../views/SimilarNovelDatas.vue'
import SearchNovel from '../views/SearchNovel.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/search',
    name: 'search',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: SearchNovel
  },
  {
    path: '/novel/:id',
    component: NovelDetail
  },
  {
    path: '/siminovel/get/:id',
    component: SimilarNovelDatas
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
