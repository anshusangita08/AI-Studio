# AI Studio - Master Build Plan

Version: 1.0
Status: Living Document

---

# Project Vision

AI Studio is a production-quality Local AI Video Factory.

Everything runs locally.

No cloud AI.

Modular architecture.

Professional quality.

Simple UI.

Built for long-term maintainability.

---

# Technology Stack

Backend
- Python 3.12+
- FastAPI

Frontend
- HTMX
- Jinja2
- HTML/CSS

AI
- LM Studio (OpenAI compatible API)

Image
- Pillow
- Fooocus (future)

Speech
- Edge TTS

Video
- FFmpeg

---

# Development Rules

Never redesign architecture unless explicitly instructed.

Modify the minimum number of files.

Reuse existing services.

Never invent APIs.

Inspect implementations before coding.

Keep functions small.

Keep modules independent.

Prefer extending existing services.

Never rewrite working code.

Never break previous milestones.

---

# Standard Workflow

## Phase 1 — Planning

Before coding

- Inspect repository
- Read existing implementation
- Identify affected files
- Produce:
  - Existing components
  - Current capabilities
  - Missing components
  - Risks
  - Test strategy

Wait for approval.

Never code during planning.

---

## Phase 2 — Implementation

Implement only requested milestone.

Minimal file changes.

No architecture changes.

Production quality.

---

## Phase 3 — Validation

Always run

python -m pytest tests/ -v

python launcher.py

Fix failures.

Repeat until successful.

---

## Phase 4 — Manual Testing

Never mark milestone complete until manual testing passes.

Always verify

✓ launcher starts

✓ pages render

✓ buttons work

✓ redirects work

✓ persistence works

✓ new feature works

✓ no regression

---

## Git Workflow

Feature development

develop branch

Stable releases

main branch

After milestone completion

git add .

git commit

git push origin develop

Merge

develop

↓

main

↓

push

↓

checkout develop

↓

merge main

↓

push develop

---

# Current Repository Structure

Services

app/services/

Routes

app/ui/

Templates

app/ui/templates/

Tests

tests/

Workspace

workspace/projects/

---

# Existing Services

ProjectService

Responsibilities

- Create project
- Rename project
- Delete project
- Validate names
- Reserved names
- Duplicate checking
- Project listing

StoryService

Responsibilities

- Read story
- Save story
- Story persistence
- Story paths

---

# Current Completed Milestones

## Milestone 001–006

Foundation

Runtime

Configuration

Hardware detection

Web UI

Project architecture

(Already completed)

---

## Milestone 007

Project Manager

Completed

Includes

✓ Create Project

✓ Rename Project

✓ Delete Project

✓ Reserved names

✓ Duplicate validation

✓ Empty validation

✓ Friendly validation

✓ Tests

✓ Manual verification

---

## Milestone 008.1

Story Editor

Completed

Includes

✓ StoryService

✓ Story routes

✓ Story editor page

✓ story.md persistence

✓ GET story

✓ POST story

✓ Save story

✓ Load story

✓ Manual testing

✓ Tests

---

## Maintenance

Completed

Delete confirmation dialog

Browser confirmation

No backend changes

Manual verified

---

# Remaining Build Plan

---

# Milestone 008.2

Story Generation (Mock)

Purpose

Complete story generation workflow before AI integration.

Implement

✓ Generate Story button

✓ Mock story generation

✓ Fill editor

✓ Overwrite confirmation

✓ User edits generated story

✓ Save normally

No LM Studio.

---

# Milestone 008.3

LM Studio Integration

Replace mock generation.

Keep identical UI.

Implement

LM Studio API client

Prompt building

Streaming (optional)

Error handling

Retry

Timeouts

---

# Milestone 009

Story Templates

Multiple templates

Adventure

Kids

Fantasy

Educational

Sci-Fi

Custom

---

# Milestone 010

Character Manager

Characters

Names

Descriptions

Age

Appearance

Consistency

Storage

---

# Milestone 011

Scene Planner

Break story

Scenes

Ordering

Duration

Scene editing

---

# Milestone 012

Prompt Generator

Convert scenes

↓

Image prompts

Negative prompts

Styles

Aspect ratios

---

# Milestone 013

Image Engine

LM Studio prompts

Fooocus

Generate images

Retry

Progress

---

# Milestone 014

Speech Engine

Edge TTS

Voice selection

Preview

Narration generation

---

# Milestone 015

Subtitle Engine

Generate subtitles

Timing

SRT

ASS

---

# Milestone 016

Video Timeline

Images

Narration

Music

Transitions

Timeline editing

---

# Milestone 017

Video Rendering

FFmpeg

Render

Progress

Cancellation

Retry

---

# Milestone 018

Project Dashboard

Progress

Assets

Statistics

History

---

# Milestone 019

Asset Library

Images

Audio

Video

Cleanup

Reuse

---

# Milestone 020

Pipeline

One-click generation

Story

↓

Scenes

↓

Images

↓

Narration

↓

Video

---

# Milestone 021

Settings

LM Studio

FFmpeg

Fooocus

Workspace

Defaults

---

# Milestone 022

Logs

Viewer

Filtering

Search

Download

---

# Milestone 023

Performance

Parallel generation

Caching

GPU detection

Memory optimization

---

# Milestone 024

Packaging

Installer

Portable

Configuration

Documentation

---

# Quality Rules

Every milestone

Must compile

Must run

Must pass tests

Must be manually tested

Must not break previous milestones

---

# Testing Checklist

Always verify

✓ python launcher.py

✓ python -m pytest tests/ -v

✓ Manual UI

✓ Persistence

✓ Navigation

✓ Regression

---

# Definition of Done

A milestone is complete only when

✓ Code implemented

✓ Tests pass

✓ Launcher starts

✓ Manual testing completed

✓ No regressions

✓ Git committed

✓ develop pushed

✓ merged to main

✓ develop synced again