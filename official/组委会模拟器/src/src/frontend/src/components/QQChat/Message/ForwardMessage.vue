<template>
  <div class="fakeqq-message fakeqq-forward" :class="[onright ? 'right-chat' : 'left-chat']">
    <div :style="{ 'background-image': `url(${avatar})` }" class="fakeqq-message__avatar"></div>
    <div class="fakeqq-message__content">
      <div class="fakeqq-message__name">{{ name }}</div>
      <div class="fakeqq-message__bubble">
        <div class="fakeqq-message__bubble-arrow"></div>
        <div class="fakeqq-forward__title">{{ title }}的聊天记录</div>
        <div class="fakeqq-forward__content">
          <div v-for="content in contents" :key="contents.indexOf(content)">
            {{ content }}
          </div>
        </div>
        <div class="fakeqq-forward__count">查看{{ counts ? counts : contents.length }}条转发消息</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ForwardMessage',
  props: {
    name: { type: String, required: true },
    avatar: { type: String, required: true },
    title: { type: String, required: true },
    contents: { type: Array, required: true },
    counts: { type: [Number, String], default: 0 },
    onright: Boolean,
  },
})
</script>
