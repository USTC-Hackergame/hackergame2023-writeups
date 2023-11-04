<template>
  <div class="fakeqq-message" :class="[onright ? 'right-chat' : 'left-chat']">
    <div v-if="avatar" :style="{ 'background-image': `url(${avatar})` }" class="fakeqq-message__avatar"></div>
    <div v-else class="fakeqq-message__avatar">
      <span class="fakeqq-message__text-avatar">{{ name[0] }}</span>
    </div>
    <div class="fakeqq-message__content">
      <div class="fakeqq-message__name">{{ name }}</div>
      <img :src="src" :style="{ 'max-width': maxWidth }" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ImageMessage',
  props: {
    name: { type: String, required: true },
    avatar: String,
    src: { type: String, required: true },
    onright: Boolean,
    maxWidth: { type: String, default: '250px' },
  },
})
</script>
