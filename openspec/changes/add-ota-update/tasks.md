## 1. Implementation
- [ ] 1.1 Create `openspec/changes/add-ota-update/specs/firmware/spec.md` with ADDED requirements (done)
- [ ] 1.2 Design API (or MQTT topics) for: upload firmware, publish new release, device poll/notify, and status reporting
- [ ] 1.3 Implement server-side endpoints / topics
- [ ] 1.4 Implement device-side handling (simulator): check for updates, download, verify signature, apply update, report status
- [ ] 1.5 Add firmware signing & verification utilities (test key pair in repo for lab use)
- [ ] 1.6 Add unit tests for server utilities and device update logic
- [ ] 1.7 Add integration test: simulated device performs full OTA flow against test server
- [ ] 1.8 Add CI job to run OTA integration test in matrix (if resources permit)

## 2. Validation
- [ ] 2.1 Run `openspec validate add-ota-update --strict` and resolve issues
- [ ] 2.2 Ensure all tasks above are checked before requesting approval

## 3. Rollout
- [ ] 3.1 Add documentation & usage examples (`examples/ota/`)
- [ ] 3.2 After merging, optionally archive the change once deployed
