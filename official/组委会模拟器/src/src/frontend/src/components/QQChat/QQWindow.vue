<template>
  <div class="fakeqq-window">
    <div class="fakeqq-header">
      <img :src="require('@/assets/svgs/back.svg')" class="fakeqq-header__bth" @click="exitWindowFullScreen" />
      <span class="fakeqq-header__title">
        <img :src="require('@/assets/svgs/ear.svg')" class="fakeqq-header__bth" />
        {{ title }}{{ count ? '（还有 ' + count + ' 条消息）' : '' }}
      </span>
      <img :src="require('@/assets/svgs/menu.svg')" class="fakeqq-header__bth" @click="setWindowFullScreen" />
    </div>
    <div class="fakeqq-container">
      <slot></slot>
    </div>
    <div class="fakeqq-footer">
      <form class="fakeqq-footer__input">
        <textarea class="fakeqq-footer__input-text" contenteditable="true"></textarea>
        <button class="fakeqq-footer__input-btn" type="reset">发送</button>
      </form>
      <div class="fakeqq-footer__btn">
        <img :src="require('@/assets/svgs/voice.svg')" />
        <img :src="require('@/assets/svgs/pic.svg')" />
        <img :src="require('@/assets/svgs/camera.svg')" />
        <img :src="require('@/assets/svgs/redpack.svg')" />
        <img :src="require('@/assets/svgs/emoji.svg')" />
        <img :src="require('@/assets/svgs/more.svg')" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'QQWindow',
  props: {
    title: { type: String, required: true },
    count: { type: [String, Number], default: '' },
  },
  methods: {
    // 启动全屏
    setWindowFullScreen() {
      document.documentElement.requestFullscreen()
    },
    // 退出全屏
    exitWindowFullScreen() {
      document.exitFullscreen()
    },
  },
})
</script>

<style lang="scss">
@import './fakeqq.scss';
</style>
