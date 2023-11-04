<template>
  <div class="fakeqq-message" :class="[onright ? 'right-chat' : 'left-chat']">
    <div v-if="avatar" :style="{ 'background-image': `url(${avatar})` }" class="fakeqq-message__avatar"></div>
    <div v-else class="fakeqq-message__avatar">
      <span class="fakeqq-message__text-avatar">{{ name[0] }}</span>
    </div>
    <div class="fakeqq-message__content" :onclick="click">
      <div class="fakeqq-message__name">{{ name }}</div>
      <a ref="file" target="_blank" style="text-decoration: none; color: #000">
        <div class="fakeqq-message__bubble" style="cursor: pointer">
          <div class="fakeqq-message__bubble-arrow"></div>
          <div class="fakeqq-file__content">
            <div class="fakeqq-file__info">
              <div class="fakeqq-file__name">{{ filename }}</div>
              <div class="fakeqq-file__size">{{ filesize }}</div>
            </div>
            <div class="fakeqq-file__icon">
              <img :src="fileicon" />
            </div>
          </div>
        </div>
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'FileMessage',
  props: {
    name: { type: String, required: true },
    avatar: String,
    filename: { type: String, required: true },
    filesize: { type: String, required: true },
    fileicon: { type: String, required: true },
    href: { type: String, default: '' },
    onright: Boolean,
    click: { type: Function, default: function () {} }, // eslint-disable-line
  },
  mounted() {
    if (this.href) {
      const file = this.$refs.file as HTMLAnchorElement
      file.href = this.href
    }
  },
})
</script>
