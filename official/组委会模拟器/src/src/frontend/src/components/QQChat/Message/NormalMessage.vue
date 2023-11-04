<template>
  <div class="fakeqq-message" :class="[onright ? 'right-chat' : 'left-chat']">
    <div v-if="avatar" :style="{ 'background-image': `url(${avatar})` }" class="fakeqq-message__avatar"></div>
    <div v-else class="fakeqq-message__avatar">
      <span class="fakeqq-message__text-avatar">{{ name[0] }}</span>
    </div>
    <div class="fakeqq-message__content">
      <div class="fakeqq-message__name">{{ name }}</div>
      <div class="fakeqq-message__bubble" @click="revoke">
        <div class="fakeqq-message__bubble-arrow"></div>
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'NormalMessage',
  props: {
    name: { type: String, required: true },
    avatar: String,
    onright: Boolean,
  },
  emits: ['revoke'],
  methods: {
    revoke(payload: MouseEvent) {
      const target = payload.target
      if (target instanceof HTMLElement && target.tagName === 'A') {
        return
      }
      this.$emit('revoke')
    },
  },
})
</script>
